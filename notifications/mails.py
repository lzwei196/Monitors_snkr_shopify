import smtplib
import traceback
from email.message import EmailMessage
from util.decorators import *

class Email():

    def __init__(self, email, pwd, smpt_server='smtp.gmail.com', port=465):
        try:
            self.email = email
            self.pwd = pwd
            self.smpt_server = smpt_server
            self.port=port
            self.server = smtplib.SMTP_SSL(smpt_server, port)
            self.server.ehlo()
            self.server.login(email, pwd)
            self.email=email
        except:
            print(f'failed to login via {smpt_server} from {email}')
            raise


    @debug
    def send_msg(self, to, subject, body):
        try:
            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['From'] = self.email
            msg['To'] = to
            self.server.send_message(msg)
        except smtplib.SMTPServerDisconnected:
            self.server = smtplib.SMTP_SSL(self.smpt_server, self.port)
            self.server.ehlo()
            self.server.login(self.email, self.pwd)
            self.email=self.email
            self.send_msg(to, subject, body)
        except:
            traceback.print_exc()
            print(f'failed to send email to {to}')



    def __del__(self):
        self.server.quit()


if __name__=='__main__':
    pass