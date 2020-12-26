from requests_html import HTMLSession
import json
import datetime
import time
from pprint import pprint
import selenium_wrapper.selenium_support as ss
from util.decorators import *
from util.request_bot import Requests_bot






TIMOUT=15

class LV_requests(Requests_bot):
    @debug
    def __init__(self):
        super(LV_requests, self).__init__(TIMEOUT=TIMOUT)


    def login(self):
        data='{"login":"yaqixyz@gmail.com","password":"Canada2911."}'
        self.session.headers.update({'referer': 'https://ca.louisvuitton.com/eng-ca/homepage',
                                     'origin': 'https://ca.louisvuitton.com',
                                     'sec-fetch-site': 'same-site',
                                     'sec-fetch-mode': 'cors',
                                     'sec-fetch-dest': 'empty',
                                     'authority': 'api.louisvuitton.com',
                                     })
        # response = self.options('https://api.louisvuitton.com/api/eng-ca/account/login', timeout=TIMOUT)
        response = self.post('https://api.louisvuitton.com/api/eng-ca/account/login', timeout=TIMOUT, data=data)

    @debug
    def set_cookies(self):
        self.session.headers.update({'referer': 'https://www.google.com/',
                                     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
        response = self.get('https://ca.louisvuitton.com/eng-ca/homepage')
        response = self.get('https://ca.louisvuitton.com/akam-sw-policy.json')
        response = self.get('https://api.louisvuitton.com/api/eng-ca/account/user')


    @timer
    @exception_handler_LV
    def atc(self, product_url, identifier, skuId, test_stock=False):
        data = {"catalogRefIds":[skuId],"productId":identifier,"quantity":1}
        response = self.get(product_url)
        response = self.options('https://api.louisvuitton.com/api/eng-ca/cart', timeout=TIMOUT)


        headers = {
            'authority': 'api.louisvuitton.com',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://ca.louisvuitton.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': product_url,
            'accept-language': 'en-US,en;q=0.9'}
        response = self.put('https://api.louisvuitton.com/api/eng-ca/cart', json=data, headers=headers)
        if test_stock is True:
            return response
        response = self.get('https://api.louisvuitton.com/api/eng-ca/cart/mini')
        response = self.get('https://secure.louisvuitton.com/akam-sw-policy.json')

        param={'storeLang':'eng - ca',
               'pageType':'cart',
               'logout':'',
               '_': '1607823502708',
               '_': '1607769168', #ak_wfSession
               '_': '1607823501'
               }
        response = self.options('https://secure.louisvuitton.com/ajaxsecure/loadCommerceHeadersJson.jsp', params=param)

        param.pop('_')
        response = self.get('https://secure.louisvuitton.com/ajaxsecure/commerce/microShoppingBag.jsp', params=param)


if __name__=='__main__':
    # data = {"catalogRefIds": ['1A8K7E'], "productId": 'nvprod2480036v', "quantity": 1}
    # response = requests.put('https://api.louisvuitton.com/api/eng-ca/cart', json=data)
    # print(response, 'cart put', response.text)
    # exit(0)
    bot = LV_requests()
    bot.set_cookies()
    bot.login()
    # bot.atc('https://ca.louisvuitton.com/eng-ca/products/spring-street-monogram-vernis-nvprod1280190v',
    #         'nvprod1280190v',
    #         'M90468', test_stock=False)