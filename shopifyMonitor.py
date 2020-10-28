import time
import json
import requests
from shopifyWebhook import notifyDisc, notifyDisc_unfilteded
from random import randint
from flask_sqlalchemy_db import db, Sites
import random
import concurrent.futures
import os
def load_proxy(file_path: str):
    """
           Reads a text file with proxies
           :param file_path: Path to proxy file with proxies in <user>:<pas>@<ip>:<port> format each on one line
           """
    lst = []
    if file_path:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lst = [x for x in file.read().split('\n') if x.strip()]
                return lst
        else:
            print('File: {}. Does not exist.'.format(file_path))

def parse_proxy(proxy):
    ip, port, name, password = proxy.split(':')
    return {
    "http": f"http://{name}:{password}@{ip}:{port}",
    "https": f"http://{name}:{password}@{ip}:{port}",
    'ftp_proxy':f"http://{name}:{password}@{ip}:{port}"
    }

def loadJSON():
    try:
        acquiredList = []
        opt = Sites.query.all()
        for val in opt:
            acquiredList.append({"Name": val.name, "status": val.status})
        return acquiredList
    except Exception as e:
        print(e)


def findDiff(data1, data2):
    newStock = list(set(data1) - set(data2))
    return newStock


def returnCart(data, i):
    cartList = []
    for cart in data:
        if cart["available"]:
            cartLink = i+"/cart/"+str(cart['id'])+":1"
            cartList.append({"size": str(cart['title']), "cartLink": cartLink})
    return cartList


def callNotif(data, i, val):

    price = data["variants"][0]["price"]

    cartList = returnCart(data["variants"], i)

    imageUrl = data["imageUrl"]

    handle = data["handle"]

    title = data["title"]

    link = i + "/products/" + handle
    
    if val:
            notifyDisc(cartList, imageUrl, link, title, price)
    else:
        notifyDisc_unfilteded(cartList, imageUrl, link, title, price)



def checkRestock(dataList, sneakerData, i, site):

    try:
        for data, value in sneakerData.items():
            try:
                for idx, item in enumerate(value["variants"]):
                    if item["available"] == "false" and dataList[data]["variants"][idx]["available"] == "true":
                        callNotif(dataList[data], i)
                        break
            except Exception as e:
                continue
        with open(site + ".txt", 'w') as outfile:
            json.dump(dataList, outfile)
    except Exception as e:
        pass


def loadProxy():
    with open("proxy.json") as proxy_list:
        proxy = json.load(proxy_list)
        # print(proxy)
        proxiesid = {'http': "http://" + random.choice(proxy)}
    return proxiesid

def loadKeyword():
    with open("keywords.json") as keyword:
        keyword_string = json.load(keyword)
    return keyword_string

def checkStock(num):
    proxy = load_proxy('proxy.text')
    while True:
        shopifyList = loadJSON()
        if num == 0 or num % 2 == 0:
            the_list = shopifyList
        else:
            shopifyList.reverse()
            the_list = shopifyList
        try:
            # go through all the sites
            for i in the_list:
                the_proxy = parse_proxy(random.choice(proxy))
            #for i in (shopifyList):
                #i = secrets.choice(shopifyList)
                site = i['Name'].replace(".", "").replace("//", "").replace(":", "")
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
                source = requests.get(i['Name']+"/products.json", headers=headers, proxies=the_proxy).text
                soup = json.loads(source)
                listData = (soup["products"])
                idList = {}

# grab the general data for the products in the site
                for idx, data in enumerate(listData):
                        if data['images']:
                            imageUrl = data['images'][0]['src']
                        else:
                            imageUrl = 'no image available'

                        handle = data['handle']
                        itemData = {"variants": data["variants"],
                                    "imageUrl": imageUrl, "handle": handle,
                                    "title": data["title"]}

                        dictKey = {str(data["id"]): itemData}
                        idList.update(dictKey)
                    #load the records from database
                sneakerDatas = json.loads(i['status'])
                listKeys = list(sneakerDatas.keys())
                # compare whether if this product is new
                idKey = list(idList.keys())
                newStock = findDiff(idKey, listKeys)
                keyword = loadKeyword()
                filter_boo = True
                if len(newStock) != 0:
                    try:
                        for key in newStock:
                            newItem = {str(key): idList[str(key)]}
                            sneakerDatas.update(newItem)
                            newData = idList[str(key)]
                            for kw in keyword:
                                if kw in idList[str(key)]["handle"].lower():
                                    callNotif(newData, i["Name"], True)
                                    filter_boo = False
                                    break
                            if filter_boo:
                                callNotif(newData, i["Name"], False)
                        site_update = Sites.query.filter_by(name=i['Name']).first()
                        site_update.status = json.dumps(sneakerDatas)
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        print(i)
                        print(soup)
                    # check if there is new restock
                    # checkRestock(idList, sneakerDatas, i['Name'], site)
            time.sleep(randint(15, 30))

        except Exception as e:
                print(e)
                time.sleep(randint(50, 100))

if __name__ == '__main__':
    try:
        with concurrent.futures.ThreadPoolExecutor() as player:
            for num in range(10):
                player.submit(checkStock, num)
    except Exception as e:
        print(e)

