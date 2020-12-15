from requests_html import HTMLSession
import json
import datetime
import time
from pprint import pprint
import selenium_wrapper.selenium_support as ss
from util.decorators import *
import requests





class LV():
    @debug
    def __init__(self):
        self.session = HTMLSession()


    @debug
    def set_cookies(self):
        self.session.headers.update({'referer': 'https://www.google.com/',
                                     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'})
        response = self.session.get('https://ca.louisvuitton.com/eng-ca/homepage')
        print(response)

        response = self.session.get('https://ca.louisvuitton.com/akam-sw-policy.json')
        print(response)
        pprint(response.json())
        response = self.session.get('https://api.louisvuitton.com/api/eng-ca/account/user')
        print(response)
        pprint(response.json())

    @debug
    def atc(self, product_url, identifier, skuId, test_stock=False):
        data = {"catalogRefIds":[skuId],"productId":identifier,"quantity":1}
        response = self.session.get(product_url)
        print(response, 'url')
        response = self.session.options('https://api.louisvuitton.com/api/eng-ca/cart')
        print(response, 'cart')

        headers = {
            'authority': 'api.louisvuitton.com',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://ca.louisvuitton.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ca.louisvuitton.com/eng-ca/products/game-on-classic-bikini-bottoms-nvprod2550060v',
            'accept-language': 'en-US,en;q=0.9'}
        response = self.session.put('https://api.louisvuitton.com/api/eng-ca/cart', json=data, headers=headers)
        print(response, 'cart put', response.text)
        print(response.status_code==200)
        if test_stock is True:
            return response
        response = self.session.get('https://api.louisvuitton.com/api/eng-ca/cart/mini')
        print(response, 'mini')
        response = self.session.get('https://secure.louisvuitton.com/akam-sw-policy.json')
        print(response, 'policy')

        param={'storeLang':'eng - ca',
               'pageType':'cart',
               'logout':'',
               '_': '1607823502708',
               '_': '1607769168', #ak_wfSession
               '_': '1607823501'
               }
        response = self.session.options('https://secure.louisvuitton.com/ajaxsecure/loadCommerceHeadersJson.jsp', params=param)
        print(response, 'loadCommerceHeadersJson', response.text)


        param.pop('_')
        response = self.session.get('https://secure.louisvuitton.com/ajaxsecure/commerce/microShoppingBag.jsp', params=param)
        print(response,response.text)


if __name__=='__main__':
    # data = {"catalogRefIds": ['1A8K7E'], "productId": 'nvprod2480036v', "quantity": 1}
    # response = requests.put('https://api.louisvuitton.com/api/eng-ca/cart', json=data)
    # print(response, 'cart put', response.text)
    # exit(0)
    bot = LV()
    #bot.set_cookies()
    bot.atc('https://ca.louisvuitton.com/eng-ca/products/trocadero-richelieu-nvprod2480036v',
            'nvprod2480036v',
            '1A8K7E', test_stock=True)