from email.message import EmailMessage
import smtplib
import os.path
import mimetypes
import getpass

sender = "me@example.com"
recipient = "you@example.com"
message = EmailMessage()

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hey there!
...
... I'm learning to send emails using Python!"""
message.set_content(body)

attachment_path = "bride.jpg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap: 
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))
print(message)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')#Set your SMTP server
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass('Password? ')#Enter your password
print(mail_pass)
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()