import requests
import json
import datetime
import time
from shopifyMonitor import load_proxy, parse_proxy
import random
from selenium_wrapper.selenium_support import *
from requests_html import HTMLSession
import traceback
import bestbuy_bot.args as args
from util.decorators import *
########################### General param ##########################
####REPLACE the address, credit card info in the submit shipping, payment and order section
#the cookie will be expired in an hour, haven't tested much, but this seems to be the case
#xtx is has to match
#the easiest way maybe go to the site and go through the whole atc and submit order process and manually grab all the information
#currently You should be getting res from each step, if not, change the cookie

secure_res="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"
url = "https://www.bestbuy.ca"
order_url = "https://www.bestbuy.ca/api/checkout/checkout/orders"
#bestbuy restocks at each quater
the_time = ["14","15","59","0","29","30","44","45","55","56"]
sku = "14962185"
#14962193 14962184
xtx = args.xtx
####################################################################
purchased=False





class bestbuy:
    @debug
    def __init__(self,proxy=None, proxyornot=False, oneonly = True):
        self.oneonly = oneonly
        self.proxy = proxy
        self.session = HTMLSession()
        self.proxyornot = proxyornot
        self.timeout=10
        self.set_cookies()

    def start_bot(self):
        lineItems = {}
        while True:
            lineItems = self.atc()
            if lineItems[0]["total"] != 0 :
                obj = self.submit_shipping(lineItems)
                id = obj[0]
                totalPurchasePrice = obj[1]
                self.submit_payment(id)
                if self.submit_order(id, totalPurchasePrice) and self.oneonly:
                    global purchased
                    purchased = True
                    return
                else:
                    traceback.print_exc()
                    pass
            else:
                print('sleeping 10 before trying to add to cart again')
                sleep(10)

    @debug
    def set_cookies(self):
        crawler = Bestbuy('../chromedriver.exe', headless=True)
        crawler.login()
        cookies = crawler.browser.get_cookies()
        for cookie in cookies:
            self.session.cookies.set(cookie['name'], cookie['value'])

        self.session.cookies.set('tx', xtx)
        for name, val in self.session.cookies.items():
            print(name, val)
        print('ok')
        response = self.session.get('https://www.bestbuy.ca/checkout/?qit=1')
        print(response, response.text)

    @debug
    @exception_handler
    def atc(self):
        add_to_cart_url = "https://www.bestbuy.ca/api/basket/v2/baskets"
        data = {"lineItems":[{"sku":"","quantity":1}]}
        data["lineItems"][0]["sku"] = sku
        headers = args.atc_headers
        if self.proxyornot:
            r = self.session.post(add_to_cart_url, data=json.dumps(data), headers=headers, proxies=self.proxy)
        else:
            r = self.session.post(add_to_cart_url, data=json.dumps(data), headers=headers)
        print('############')
        print('adding' + sku + ' to cart')
        print(r.text)
        lineItems = json.loads(r.text)["shipments"][0]["lineItems"][0]
        obj ={}
        lineItems_format = []
        obj["lineItemType"]="Product"
        obj["name"]=lineItems["sku"]["product"]["name"]
        obj["offerId"]=lineItems["sku"]["offer"]["id"]
        obj["quantity"]= 1
        obj["sellerId"] = "bbyca"
        obj["sku"] = lineItems["sku"]["id"]
        obj["total"] = json.loads(r.text)["shipments"][0]["totalPrice"]
        lineItems_format.append(obj)
        #print(lineItems_format[0]["total"])
        return  lineItems_format

    @debug
    def start_checkout(self):
        headers = args.atc_headers
        r = self.session.get("https://www.bestbuy.ca/checkout/?qit=1#/en-ca/shipping/", headers=headers)
        print(r.text)
        print(self.session.cookies.get_dict())

    @debug
    @exception_handler
    def submit_shipping(self,lineItems):
        data = {"email":args.email,"shippingAddress":{"address":args.address,"apartmentNumber":args.apartmentNumber
            ,"city":args.city,"country":args.country,"firstName":args.firstName,"lastName":args.lastName,"phones":[{"ext":args.ext,"phone":args.phone}]
            ,"postalCode":args.postalCode,"province":args.province}}
        data["lineItems"] = lineItems

        shipping_headers = {
            "accept": "application/vnd.bestbuy.checkout+json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-CA",
            "content-type": "application/json",
            "content-length":"493",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Host": "www.bestbuy.ca",
             "referer": "https://www.bestbuy.ca/checkout/",
            "x-dtreferer": "https://www.bestbuy.ca/checkout/#/en-ca/shipping/QC/H3G0E1",
            "x-tx":xtx
        }

        timeout=self.timeout
        if self.proxyornot:
            r = self.session.post(order_url, headers=shipping_headers, json=data, proxies=self.proxy, cookies=self.session.cookies, timeout=timeout)
        else:
            r = self.session.post(order_url,headers=shipping_headers,json=data, cookies=self.session.cookies, timeout=timeout)
        print("#######################")
        print('submit shipping')
        print(r.text)
        id = json.loads(r.text)["id"]
        totalPurchasePrice = json.loads(r.text)["totalPurchasePrice"]
        print('exiting at shipping as this is a test run, find this line and comment out the next line if you want real runs')
        #exit(0)
        return [id, totalPurchasePrice]

    @debug
    @exception_handler
    def submit_payment(self,id):
        url = "https://www.bestbuy.ca/api/checkout/checkout/orders/"+id+"/payments"
        data = {"email":args.email,
                "payment":{"creditCard":{"billingAddress":{"address":args.address,"apartmentNumber":args.apartmentNumber
                    ,"city":args.city,args.country:"CA","email":args.email,"firstName":args.firstName,"lastName":args.lastName,
                                                           "phones":[{"ext":args.ext,"phone":args.phone}],"postalCode":args.postalCode,
                                                           "province":args.province},
                                         "cardNumber":args.cardNumber,
                                         "cardType":args.cardType,"cvv":args.cvv,"expirationMonth":args.expirationMonth,"expirationYear":args.expirationYear}}}

        headers=args.order_headers
        timeout = self.timeout
        if self.proxyornot:
            r = self.session.put(url,headers=headers,json=data, proxies = self.proxy, cookies=self.session.cookies, timeout=timeout)
        else:
            r = self.session.put(url,headers=headers,json=data, cookies = self.session.cookies, timeout=timeout)
        print(r.text)

    @debug
    @exception_handler
    def submit_order(self,id,totalPurchasePrice):
        url = "https://www.bestbuy.ca/api/checkout/checkout/orders/submit"
        headers=args.order_headers
        data = {"cvv":args.cvv,"email":args.email,"secureAuthenticationResponse":secure_res}
        data["totalPurchasePrice"] = totalPurchasePrice
        data["id"] = id
        timeout=self.timeout
        if self.proxyornot:
            r = self.session.post(url, headers=headers, json=data, proxies=self.proxy, cookies = self.session.cookies, timeout=timeout)
        else:
            r = self.session.post(url, headers=headers,json=data, cookies = self.session.cookies, timeout=timeout)
        order_detail = json.loads(r.text)
        print("#################")
        print('submit order')
        print(order_detail)
        if order_detail['orderNumber'] != 'null' and order_detail['orderNumber'] != None:
            print('order ' + order_detail['orderNumber'] + " Successfully placed")
            return True
        else:
            print('order failed, retrying')
            return False
if __name__ == '__main__':
    proxies = load_proxy('proxy.text')
    while True:
        the_proxy = parse_proxy(random.choice(proxies))
        try:
            #When creating the bestbuy obj, its default to use proxy and only checkout once, u can pass in different params.
            bestbuy = bestbuy(the_proxy)
            bestbuy.start_bot()
            print('exiting cuz bestbuy finished running without exceptions')
            exit(0)
        except Exception as e:
            if purchased:
                print('exiting cuz purchased was flagged true')
                exit(0)
            print(e)
