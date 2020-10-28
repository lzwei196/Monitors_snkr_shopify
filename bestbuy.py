import json
import random
import requests
import concurrent.futures
from flask_sqlalchemy_db import db, best_buy
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from collections import OrderedDict
from shopifyWebhook import notifyDisc_bestbuy
import time
from random import randint
import concurrent.futures

def loadProxy():
    with open("proxy.json") as proxy_list:
        proxy = json.load(proxy_list)
        # print(proxy)
        proxiesid = {'http': "http://" + random.choice(proxy)}
    return proxiesid

def best_buy_monitor():
    while True:
                software_names = [SoftwareName.CHROME.value]
                operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
                user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

                best_buy_base_url = "https://www.bestbuy.ca/en-ca/product/"
                best_buy_api_url = "https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&postalCode=H3J2T7&skus="
                old_status_db = best_buy.query.all()

                for item in old_status_db:
                    id = item.id_number
                    name = item.name
                    shipping = item.shipping
                    instore = item.instore
                    try:
                        #proxy = loadProxy()
                        headers = {
                            'upgrade-insecure-requests': '1',
                            'cache-control': 'no-cache',
                            'Pragma': 'no-cache',
                            'user-agent': user_agent_rotator.get_random_user_agent(),
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                            'sec-fetch-site': 'none',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9'
                        }
                        url = best_buy_api_url + id
                        r = requests.get(url=url,headers=headers).text.encode().decode('utf-8-sig')
                        avail = json.loads(r)["availabilities"][0]
                        shipping_status = avail["shipping"]["purchasable"]
                        instore_status = avail["pickup"]["purchasable"]
                        if str(shipping_status) != str(shipping )or str(instore_status)!=(instore):
                            if shipping_status == True:
                                link = best_buy_base_url+id
                                notifyDisc_bestbuy(name, link,"Shipping", str(True))
                            update = best_buy.query.filter_by(id_number=id).first()
                            update.shipping = str(shipping_status)
                            db.session.commit()

                            if instore_status == True:
                                link = best_buy_base_url+id
                                notifyDisc_bestbuy(name, link,"instore", str(True))
                            update = best_buy.query.filter_by(id_number=id).first()
                            update.instore = str(instore_status)
                            db.session.commit()
                    except Exception as e:
                        print(e)

                time.sleep(randint(5,30))

if(__name__ == "__main__"):
    try:
        with concurrent.futures.ThreadPoolExecutor() as player:
            for num in range(10):
                player.submit(best_buy_monitor)
    except Exception as e:
        print(e)
