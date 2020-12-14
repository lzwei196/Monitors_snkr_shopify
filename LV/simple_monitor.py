from requests_html import HTMLSession
import sys
import platform
from notifications.messenger import Messenger
from notifications.mails import Email
from notifications.discord import send_webhook
from time import sleep
import datetime as dt

MESSENGER_LIST={'Katherine Nguyen': '100003870432163',
                'Jolin Lu': '100009501767563'}

GMAIL_LIST={'Katherine Nguyen': 'nhunga161@gmail.com',
                'Jolin Lu': 'Jolin.luzhang@gmail.com'}

ALERTED={}


API_BASE='https://api.louisvuitton.com/api/eng-ca/catalog/availability/%s'

session = HTMLSession()
PRODUCT_URLS = ['https://ca.louisvuitton.com/eng-ca/products/mini-pochette-accessoires-monogram-001025',
                'https://ca.louisvuitton.com/eng-ca/products/nano-speedy-monogram-010575',
                'https://ca.louisvuitton.com/eng-ca/products/toiletry-pouch-26-monogram-canvas-000767',
                'https://ca.louisvuitton.com/eng-ca/products/pochette-accessoires-monogram-005656',
                'https://ca.louisvuitton.com/eng-ca/products/nice-nano-monogram-nvprod2320034v',
                ]
gmail=None
QUIET_PERIOD=5
if len(sys.argv) < 2:
    print('please pass in pwd as param')
    exit(0)

pwd=sys.argv[1]
email = "yaqixyzlancelot@gmail.com"
alerts_sent=0

def alert(subject, msg, url):
    for name, email_addr in GMAIL_LIST.items():
        gmail.send_msg(email_addr, subject, msg)
    send_webhook(f'LV RESTOCK via {platform.system()}', url,
                 url='https://discord.com/api/webhooks/787083663581380629/6JQWwL9jTIZntx6OeukQNkmTS0WF6lPLbXPkXYtTrPPoZRJhWoputZTfsE0bdLKahWPI')


def check():
    global ALERTED
    print(dt.datetime.now())
    for url in PRODUCT_URLS:
        identifier = url.split('-')[-1]
        api_endpoint = API_BASE % identifier
        response = session.get(api_endpoint)
        data = response.json()

        print(data)
        global gmail
        for availability in data['skuAvailability']:
            if availability['inStock'] == True:
                print('restocked')
                if gmail is None:
                    gmail=Email(email, pwd)
                msg = f'THE FOLLOWING PRODUCT HAS RESTOCKED -> {url}'
                subject = "LV RESTOCK ALERT"
                print(msg)
                if url not in ALERTED:
                    ALERTED[url]=dt.datetime.now()
                    alert(subject, msg, url)
                else:
                    minutes_diff = (dt.datetime.now() - ALERTED[url]).total_seconds() / 60.0
                    if minutes_diff > QUIET_PERIOD:
                        ALERTED[url] = dt.datetime.now()
                        alert(subject, msg, url)
                    else:
                        print(f"SKIPPING ALERT BECAUSE LAST ONE WAS SENT UNDER {minutes_diff} mins ago")

                break
            else:
                print('out of stock')

if __name__=='__main__':
    for i in range(60):
        check()
        if alerts_sent > len(PRODUCT_URLS):
            print('exiting due to notification sent')
            exit(0)
        sleep(60)


