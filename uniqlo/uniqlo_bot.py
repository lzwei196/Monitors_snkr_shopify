import requests
import json
import datetime
import time

login_url = "https://www.uniqlo.com/ca/auth/v1/login"
atc_url = "https://www.uniqlo.com/ca/api/commerce/v3/en/baskets/mine/l2s"

headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

login_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,fr;q=0.6,zh-TW;q=0.5",
            "cache-control":" max-age=0",
            "content-type": "application/x-www-form-urlencoded"
}

data = {"login_id":"lzweijinwei196%40gmail.com", "password":"Lzwei1996", "_csrf":"1ssIldpi-ML6p49In4aLDcdMrmEQalvs4YxY", "lang":"en"}
atc_data = {"basketId":"47bcee91395248869da5f55b811119c9","l2Id":"04871576","communicationCode":"42256901004000","quantity":1,"itemName":"EDO UKIYO-E LONG SLEEVE SWEATSHIRT","colorName":"OFF WHITE","sizeName":"M","pldName":"Pattern Length No Use"}

session = requests.Session()
r = session.get(login_url,headers=headers)
print(session.cookies.get_dict())
login = session.post(login_url,headers=headers,data=data)
print(login.text)
atc = session.post(atc_url,headers=headers,json=atc_data)
print(atc.text)