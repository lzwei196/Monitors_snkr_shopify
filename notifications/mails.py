import smtplib
import traceback
from email.message import EmailMessage
from util.decorators import *

class Email():

    def __init__(self, email, pwd, server='smtp.gmail.com', port=465):
        try:
            self.server = smtplib.SMTP_SSL(server, port)
            self.server.ehlo()
            self.server.login(email, pwd)
            self.email=email
        except:
            print(f'failed to login via {server} from {email}')
            raise


    @debug
    def send_msg(self, to, subject, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = to
        self.server.send_message(msg)

    def __del__(self):
        self.server.quit()


if __name__=='__main__':
    pass