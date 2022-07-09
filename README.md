# Email-Sender
Asynchronously Send Emails

## How To Use

# Config.json
Firsly goto `src/config.json`

### Configuration Options

### `-file`:
The File that will be red and extracted to send the emails

MUST BE A JSON FILE

### `-hostname`:

The Email Service Provider for your account

`For Example`: The SMTP service provider for a gmail account will be `smtp.gmail.com`

Find a SMTP serivce provider for your account [here](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html)

### `-sender`:
Your email account 
`eg`: abc123@gmail.com

### `-password`:
The password for Your email account.
Can also be an [app password](https://support.google.com/accounts/answer/185833?hl=en)

### `-timeout`:
The maximum time a request should wait
The request will be abandoned if it has taken more time than the given maximum time

### `-use_tls`:
Use Secured TLS when sending emails, [about TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)
<hr>

# email.json
This file can be anywhere in your pc, and can also be named anything you just need to change the `file` item in `config.json`
FILE MUST BE VALID JSON

It must be a list with any number of dictionary/mappings

## `Configuration`:

The dict will be a message which can be sent to multiple people
to send different messages make a new dict

### `-to`:
a list of email accounts to send email

### `-subject`:
The Title For the Message

### `-msg`:
The message to send

can be text/html or a file path

to add a file path: the message should be like this

```json
[
 {
    "to": ["person@gmail.com"],
    "subject": "Title",
    "msg": ":FILE: file.html"
 }
]
```
The program will read the file and will send it's contents

The message can be sent to multiple people by adding more accounts in the `to` list

Create a new dict to send different messages to different people
<hr>

Then Run main.py to send the emails

All The logging informattion will be written to the file `.log`
