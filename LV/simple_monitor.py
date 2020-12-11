from requests_html import HTMLSession
import sys
from notifications.messenger import Messenger
from notifications.mails import Email
from time import sleep

MESSENGER_LIST={'Katherine Nguyen': '100003870432163',
                'Jolin Lu': '100009501767563'}

GMAIL_LIST={'Katherine Nguyen': 'nhunga161@gmail.com',
                'Jolin Lu': 'Jolin.luzhang@gmail.com'}


API_BASE='https://api.louisvuitton.com/api/eng-ca/catalog/availability/%s'

session = HTMLSession()
PRODUCT_URLS = ['https://ca.louisvuitton.com/eng-ca/products/mini-pochette-accessoires-monogram-001025',
                'https://ca.louisvuitton.com/eng-ca/products/nano-speedy-monogram-010575',]
gmail=None

if len(sys.argv) < 2:
    print('please pass in pwd as param')
    exit(0)

pwd=sys.argv[1]
email = "yaqixyzlancelot@gmail.com"

def check():
    for url in PRODUCT_URLS:
        identifier = url.split('-')[-1]
        api_endpoint = API_BASE % identifier
        response = session.get(api_endpoint)
        data = response.json()
        print(data)
        for availability in data['skuAvailability']:
            if availability['inStock'] == True:
                print('restocked')
                if gmail is None:
                    gmail=Email(email, pwd)
                msg = f'THE FOLLOWING PRODUCT HAS RESTOCKED -> {url}'
                subject = "LV RESTOCK ALERT"
                print(msg)
                for name, email_addr in GMAIL_LIST.items():
                    gmail.send_msg(email_addr, subject, msg)
                break
            else:
                print('out of stock')

if __name__=='__main':
    for i in range(8):
        check()
        sleep(60)


