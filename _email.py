import smtplib
from authenticate import FileManage

auth = FileManage()

def main(message: str) -> int:
    """ for sending report """
    try:
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        """ to loading some credential """
        send_address = auth.sendSenderEmail()
        passs = auth.sendSenderPassword()
        to_address = auth.sendReceiverEmail()
        mail_server.login(send_address, passs)
        mail_server.sendmail(send_address, to_address, message)
        return 0
    except:
        return 1