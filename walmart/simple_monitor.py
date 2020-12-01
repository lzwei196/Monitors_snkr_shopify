from requests_html import HTMLSession
from pprint import pprint
from shopifyWebhook import *

session = HTMLSession()
PRODUCT_URL = 'https://www.walmart.ca/en/ip/playstation5-console/6000202198562'
PRODUCT_URL = 'https://www.walmart.ca/en/ip/lg-22-class-full-hd-tn-monitor-with-amd-freesync-1920x1080-black-22bk400h-b/PRD6S102WTJEQH4'

response = session.get(PRODUCT_URL)

if 'Out of Stock Online' in response.text:
    print('out of stock')
else:
    print('sending notification for restock')
    send_webhook('RESTOCK', PRODUCT_URL)
