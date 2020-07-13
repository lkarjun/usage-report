import re
import smtplib
from authenticate import FileManage
import email.message
import mimetypes

auth = FileManage()

def send_email(message: str) -> int:
    """ for sending report """
    try:
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        """ to loading some credential """
        send_address = auth.sendSenderEmail()
        passs = auth.sendSenderPassword()
        to_address = auth.sendReceiverEmail()
        mail_server.login(send_address, passs)
        mail_server.sendmail(send_address, to_address, message)
        mail_server.quit()
        return 0
    except:
        return 1

def generate_error_report(subject: str):
    message = email.message.EmailMessage()
    message["From"] = auth.sendSenderEmail()
    message["To"] = auth.sendReceiverEmail()
    message["Subject"] = subject
    body = "Kindly Please check Your system, and resolve it."
    message.set_content(body)
    return message