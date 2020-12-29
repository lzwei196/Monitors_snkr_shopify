from others.flask_sqlalchemy_db import db, Sites
import json
from others.shopifyWebhook import notifyDisc, notifyDisc_unfilteded
import requests
import datetime


class Shopify:
    def __init__(self, link):
        self.link = link

    def query(self):
        try:
            data = Sites.query.filter_by(name=self.link).first()
            old_data = {"Name":data.name, "status":data.status}
            return old_data
        except Exception as e:
            print(e)

    def findDiff(self,data1, data2):
        newStock = list(set(data1) - set(data2))
        return newStock

    def returnCart(self,data, i):
        cartList = []
        for cart in data:
            if cart["available"]:
                cartLink = i + "/cart/" + str(cart['id']) + ":1"
                cartList.append({"size": str(cart['title']), "cartLink": cartLink})
        return cartList

    def callNotif(self, data, i, val):

        price = data["variants"][0]["price"]

        cartList = self.returnCart(data["variants"], i)

        imageUrl = data["imageUrl"]

        handle = data["handle"]

        title = data["title"]

        link = i + "/products/" + handle

        if val:
            notifyDisc(cartList, imageUrl, link, title, price)
        else:
            notifyDisc_unfilteded(cartList, imageUrl, link, title, price)

    def loadKeyword(self):
        with open("keywords.json") as keyword:
            keyword_string = json.load(keyword)
        return keyword_string

    def checkStock(self):
        while True:
            data = self.query()
            try:
                currentDT = datetime.datetime.now()
                minute = int(currentDT.minute)
                sec = int(currentDT.second)
                if (minute % 5 == 4 and sec >= 58) or (minute % 5 == 0 and sec == 0):
                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
                    source = requests.get(data['Name'] + "/products.json", headers=headers).text
                    soup = json.loads(source)
                    listData = (soup["products"])
                    idList = {}

                    # grab the general data for the products in the site
                    for idx, data_img in enumerate(listData):
                        if data_img['images']:
                            imageUrl = data_img['images'][0]['src']
                        else:
                            imageUrl = 'no image available'

                        handle = data_img['handle']
                        itemData = {"variants": data_img["variants"],
                                    "imageUrl": imageUrl, "handle": handle,
                                    "title": data_img["title"]}

                        dictKey = {str(data_img["id"]): itemData}
                        idList.update(dictKey)
                    # load the records from database
                    sneakerDatas = json.loads(data['status'])
                    listKeys = list(sneakerDatas.keys())
                    # compare whether if this product is new
                    idKey = list(idList.keys())
                    newStock = self.findDiff(idKey, listKeys)
                    keyword = self.loadKeyword()
                    filter_boo = True
                    if len(newStock) != 0:
                        try:
                            for key in newStock:
                                newItem = {str(key): idList[str(key)]}
                                sneakerDatas.update(newItem)
                                newData = idList[str(key)]
                                for kw in keyword:
                                    if kw in idList[str(key)]["handle"].lower():
                                        self.callNotif(newData, data["Name"], True)
                                        filter_boo = False
                                        break
                                if filter_boo:
                                    self.callNotif(newData, data["Name"], False)
                            site_update = Sites.query.filter_by(name=data['Name']).first()
                            site_update.status = json.dumps(sneakerDatas)
                            db.session.commit()
                        except Exception as e:
                            print(e)
                            print(data)
                            print(soup)
                        # check if there is new restock
                        # checkRestock(idList, sneakerDatas, i['Name'], site)

            except Exception as e:
                print(e)

print("enter the link")
site = input()
shopify = Shopify(site)
shopify.checkStock()