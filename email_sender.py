from email.message import EmailMessage
from multiprocessing import context
#from email_sender import password
import ssl
import smtplib

email_sender = "aspiringkashu@gmail.com"
email_password = "barz uora whar kvtq"

email_receiver = "yavolo2513@hempyl.com"

subject = "Sending mail using python"
body = """ It is a very easy code. First import email message. Then, for security reaosns import your password and write mail format i.e sender and receiver address, subject,body etc...
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
