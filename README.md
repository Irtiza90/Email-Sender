# Email-Sender
Asynchronously Send Emails

## How To Use

## Config.json
Firsly goto `src/config.json`

### Configuration Options

### `-file`
The File that will be red and extracted to send the emails

MUST BE A JSON FILE

### `-hostname`

The Email Service Provider for your account

`example`: The SMTP service provider for a gmail account will be `smtp.gmail.com`

Find a SMTP serivce provider for your account [here](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html)

### `-sender`
Your email account 
`eg`: abc123@gmail.com


### `-password`
The password for Your email account.
Can also be an [app password](https://support.google.com/accounts/answer/185833?hl=en)

### `-timeout`
The maximum time a request should wait
The request will be abandoned if a request has taken more time than the maximum time

### `-use_tls`
Use Secured TLS when sending emails, [about TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)

###
