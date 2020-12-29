import time
import json
import requests
from bs4 import BeautifulSoup
from shopifyWebhook import notifyDisc_key
import random

def loadJSON(param):
    with open(param) as json_file:
        acquiredList = json.load(json_file)
    return acquiredList


def findDiff(data1, data2):
    newStock = list(set(data1) - set(data2))
    return newStock

def returnCart(data,i):
    cartList = []
    for cart in data:
      if cart["available"]:
        cartLink = i+"/cart/"+str(cart['id'])+":1"
        cartList.append({"size": str(cart['title']), "cartLink": cartLink})
    return cartList

def callNotif(data,i):
    price = data["variants"][0]["price"]

    cartList = returnCart(data["variants"], i)

    imageUrl = data["imageUrl"]

    handle = data["handle"]

    title = data["title"]

    link = i + "/products/" + handle

    notifyDisc_key(cartList, imageUrl, link, title, price)

def checkRestock(dataList, sneakerData, i, site):
  try:
    for data, value in sneakerData.items():
      try:
        for idx, item in enumerate (value["variants"]):
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

def checkStock():
  while True:
   try:
    num = 0
    sizeList = []
    shopifyList = loadJSON("travis.json")

#go through all the sites
    for i in shopifyList:
        site = i.replace(".", "").replace("//", "").replace(":", "")
        proxy = loadProxy()
        source = requests.get(i+"/products.json", proxies= proxy).text
        soup = json.loads(source)
        listData = (soup["products"])
        idList = {}

#grab the general data for the products in the site
        try:
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
        except Exception as e:
            print(e)
            (str(e))

#try to record the data info into local file, if exception takes place means there is info saved already
        try:
            with open(site+".txt", "x"):
                with open(site+".txt", 'w') as outfile:
                     json.dump(idList, outfile)

        except Exception as e:
            #load the product id
            sneakerDatas = loadJSON(site+".txt")
            listKeys = list(sneakerDatas.keys())
            #compare whether if this product is new
            idKey = list(idList.keys())
            newStock = findDiff(idKey, listKeys)

            if len(newStock) != 0:
              try:
                for key in newStock:
                    newData = idList[str(key)]
                    callNotif(newData, i)
                    newItem = {str(key): idList[str(key)]}
                    sneakerDatas.update(newItem)

                with open(site + ".txt", 'w') as outfile:
                    json.dump(sneakerDatas, outfile)
              except Exception as e:
                  (e)

            #check if there is new restock
            checkRestock(idList, sneakerDatas, i, site)



    time.sleep(5)
   except Exception as e:
       time.sleep(30)
       #print(i)
       #print("the error is:")
       #print(str(e))


checkStock()