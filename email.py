import smtplib


def load_credential():
    """ to load some basic credential """
    pass


def main(message: str) -> str:
    """ for sending report """
    try:
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        send_address = "techminded25@gmail.com"
        passs = "Iphone@670"
        to_address = load_credential()
        mail_server.login(send_address, passs)
        mail_server.sendmail(send_address, to_address, message)
        return str(1)
    except Exception as e:
        return f'Please contact Technical team issue is: {e}'