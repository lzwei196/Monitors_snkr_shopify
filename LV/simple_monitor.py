from requests_html import HTMLSession
import sys
import platform
from notifications.messenger import Messenger
from notifications.mails import Email
from notifications.discord import send_webhook
from time import sleep
import datetime as dt
from LV import LV_main, LV_selenium
import traceback
from persons.yi import *


MESSENGER_LIST={'Katherine Nguyen': '100003870432163',
                'Jolin Lu': '100009501767563'}

GMAIL_LIST={'Katherine Nguyen': 'nhunga161@gmail.com',
                'Jolin Lu': 'Jolin.luzhang@gmail.com',
            }

ALERTED={}
LV_selenium.AUTO_QUIT=True

API_BASE='https://api.louisvuitton.com/api/eng-ca/catalog/availability/%s'

session = HTMLSession()
PRODUCT_URLS = ['https://ca.louisvuitton.com/eng-ca/products/mini-pochette-accessoires-monogram-001025',
                'https://ca.louisvuitton.com/eng-ca/products/nano-speedy-monogram-010575',
                'https://ca.louisvuitton.com/eng-ca/products/pochette-accessoires-monogram-005656',
                'https://ca.louisvuitton.com/eng-ca/products/nice-nano-monogram-nvprod2320034v',
                # 'https://ca.louisvuitton.com/eng-ca/products/toiletry-pouch-26-monogram-canvas-000767',
                ]
gmail=None
QUIET_PERIOD=8
if len(sys.argv) < 2:
    print('please pass in pwd as param')
    exit(0)

pwd=sys.argv[1]
csv = sys.argv[2]
email = "yaqixyzlancelot@gmail.com"
yi = Yi(csv)
if platform.system() == "Windows":
    driverpath = '../chromedriver.exe'
    html_folder ='html/%s.html'
else:
    html_folder = '/tmp/LV_html/%s。html'
    driverpath = '/home/yyi/Documents/GitHub/Goodlife-class-booking/chromedriver'
lv_client=LV_selenium.LV(driverpath,yi, headless=True)

def alert(subject, msg, url):
    send_webhook(f'LV RESTOCK via {platform.system()} at {dt.datetime.now()}', url,
                 url='https://discord.com/api/webhooks/787083663581380629/6JQWwL9jTIZntx6OeukQNkmTS0WF6lPLbXPkXYtTrPPoZRJhWoputZTfsE0bdLKahWPI')
    # global gmail
    # if gmail is None:
    #     gmail = Email(email, pwd)
    # for name, email_addr in GMAIL_LIST.items():
    #     gmail.send_msg(email_addr, subject, msg)

def test_atc(product_url, identifier, skuId):
    return True
    global lv_client
    response = lv_client.atc(product_url, identifier, skuId, test_stock=True)
    if response.status_code==200:
        print(f'atc status code {response.status_code}')
        return True
    else:
        print(f'tried to add {skuId} to cart but was unable to with status code {response.status_code}')
        return False

def purchase(url):
    global lv_client
    try:
        targets=['https://ca.louisvuitton.com/eng-ca/products/mini-pochette-accessoires-monogram-001025',
                    'https://ca.louisvuitton.com/eng-ca/products/nano-speedy-monogram-010575']
        if url not in targets:
            print('skipping purchase due to not high value targets')
            return
        lv_client.atc(url)
        lv_client.purchase()
        print('purchase successful, exiting')
        exit(0)
    except LV_selenium.UnavailableException as e:
        print('Item is unavailble')
    except:
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
        lv_client.save_page(html_folder % timestamp)
        print(f"failed to purchase {url}")
        lv_client.clean_up()
        del lv_client
        lv_client = LV_selenium.LV(driverpath,yi, headless=True)


def check():
    global ALERTED
    print(dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
    for url in PRODUCT_URLS:
        identifier = url.split('-')[-1]
        api_endpoint = API_BASE % identifier
        response = session.get(api_endpoint)
        data = response.json()
        #print(data)
        global gmail
        for availability in data['skuAvailability']:
            if availability['inStock'] == True:
                # purchase(url)
                print('restocked')
                msg = f'THE FOLLOWING PRODUCT HAS RESTOCKED -> {url}'
                subject = "LV RESTOCK ALERT"
                print(msg)
                atc_allowed = test_atc(url, identifier, availability['skuId'])
                if url not in ALERTED and atc_allowed:
                    ALERTED[url]=dt.datetime.now()
                    alert(subject, msg, url)
                elif atc_allowed:
                    minutes_diff = (dt.datetime.now() - ALERTED[url]).total_seconds() / 60.0
                    if minutes_diff > QUIET_PERIOD:
                        ALERTED[url] = dt.datetime.now()
                        alert(subject, msg, url)
                    else:
                        print(f"SKIPPING ALERT BECAUSE LAST ONE WAS SENT UNDER {minutes_diff} mins ago")
                else:
                    pass
                purchase(url)
                break
            else:
                pass
                # print('out of stock')

if __name__=='__main__':
    check_frequency=30
    loops = int(60 * 60 / check_frequency) + 1
    print(loops)
    for i in range(loops):
        start = dt.datetime.now()
        check()
        seconds_elapsed = (dt.datetime.now() - start).total_seconds()
        if seconds_elapsed >= check_frequency:
            print('skippng sleep')
            continue
        else:
            sleep_time = int(check_frequency-seconds_elapsed)
            print(f'sleeping for {sleep_time}')
            sleep(sleep_time)
    lv_client.clean_up()

