import sys
import json
import asyncio

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib


async def send_mail(client: aiosmtplib.SMTP, recipients: list[str] | str, msg: MIMEMultipart, timeout: int):
    try:
        await client.send_message(
            message=msg, recipients=recipients, timeout=timeout,
        )
    
    except Exception as exc:
        print(f"[ERROR]: Sending Messages To {recipients}\nError: {exc}")


def create_message(sender: str, subject: str, message: str) -> MIMEMultipart:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["Subject"] = subject
    
    if message.startswith(":FILE:"):
        # if message is ":FILE: main.html"
        # it will read the file and will send that file instead
        
        # Converts ":FILE: main.txt" >> to >> "main.txt"
        fp = message.split(":FILE:")[1].strip()
        
        with open(fp) as f:
            message = f.read()

    msg.attach(
        MIMEText(message, "html", "utf-8")
    )
    
    return msg


async def start_sending(config: dict[str, str | int | bool], email_data: dict[str, list[str] | str]):
    # Intiliazing the client
    client = aiosmtplib.SMTP(**{
        key: config[key] for key in ("hostname", "use_tls", "username", "password")
    })

    # Creating the messages
    coroutines = []

    for creds in email_data:
        try:
            message = create_message(
                sender=config["username"], subject=creds["subject"], message=creds["msg"]
            )
            
        except FileNotFoundError:
            fp = creds["msg"].split(":FILE:")[1].strip()
            print(
                f'[ERROR]: File "{fp}" not Found.',
            )

        else:
            cor = send_mail(client, recipients=creds["to"], msg=message, timeout=config["timeout"])
            coroutines.append(cor)


    if len(coroutines) == 0:
        print("[INFO]: No Messages Sent")
        return
    
    # Connecting
    await client.connect(timeout=100)

    # Sending All The Messages
    await asyncio.gather(*coroutines)

    # Exiting
    await client.quit()


def main():
    with open("config.json") as conf:
        CONFIG: dict[str, str | bool] = json.load(conf)

    SENDER: str = CONFIG["sender"]
    CONFIG["username"] = SENDER
    send_from_f: str = CONFIG.pop("file")
    
    with open(send_from_f) as jsonf:
        try:
            json_data: list[dict[str, list[str] | str]] = json.load(jsonf)

        except json.decoder.JSONDecodeError:
            json_data = []
            print(f'[ERROR]: Could not Load JSON file "{send_from_f}"')

    with open(".log", "w") as sys.stdout: # overrides every print statement to write to the .log file
        asyncio.run(start_sending(CONFIG, json_data))


if __name__ == "__main__":
    main()
