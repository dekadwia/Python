'''
Source :
   1.https://campus.datacamp.com/courses/introduction-to-importing-data-in-python/introduction-and-flat-files-1?ex=1
   2.https://www.youtube.com/watch?v=JRCJ6RtE3xU&list=WL&index=54
   3.https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Emails/mail-demo.py
   4.https://www.youtube.com/watch?v=ODJBvbQ8rEQ&t=730s(indo)
'''
import os
import smtplib
import imghdr
from email.message import EmailMessage

sender_mail = "abriantodeka@gmail.com"
password = "fantasyabrianto123"
filename = 'Email.txt'
file = open(filename, mode = 'r')
text = file.read()
file.close()
rec_mail = list({text})

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = sender_mail
msg['To'] = 'dekadwia@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(sender_mail, password)
server.sendmail(sender_mail, rec_mail, msg.as_string())
