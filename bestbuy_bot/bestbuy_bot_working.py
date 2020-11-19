import requests
import json
import datetime
import time
from shopifyMonitor import load_proxy, parse_proxy
import random
from bestbuy_bot.selenium_support import *
from requests_html import HTMLSession
import traceback

########################### General param ##########################
####REPLACE the address, credit card info in the submit shipping, payment and order section
#the cookie will be expired in an hour, haven't tested much, but this seems to be the case
#xtx is has to match
#the easiest way maybe go to the site and go through the whole atc and submit order process and manually grab all the information
#currently You should be getting res from each step, if not, change the cookie

url = "https://www.bestbuy.ca"
order_url = "https://www.bestbuy.ca/api/checkout/checkout/orders"
#bestbuy restocks at each quater
the_time = ["14","15","59","0","29","30","44","45","55","56"]
sku = "14926557"
#14962193 14962184
cookie = \
    'GB_test=solr; bm_sz=95FEA415A742F066076ED7AFB635161A~YAAQjWCWuNp31Hd1AQAAD4fQvAmScBO8qREAX8DCqbRsvY99DMCD1vJHOkGp1MVjTDbouEEWDn2c1kcKqrX8T/' \
    '+8d3avaviFvhNE6d1MuVgKflx+itzWoSUoDRrG+LaZS59U/iap8guOyX1lSuMWFhQ+luBHMOlFh4CvfuNkts8jFRljhXUK9CFwqE/uKuPL; ' \
    'ai_user=koqaCGgiYcbNcflWDzkc59|2020-11-12T14:16:24.005Z; clientId=uouunR9XjU2qc9Wi;' \
    ' bm_mi=A4057DA7CA6C7BCA88058FF5B2FE22EF~xdRC3wwtkhspXTomE8r/XrN+z/PWy6Eh09ObCWL5o1/3umDQsGG/8vnwofCU1JZfKuf+H1SQxexxE4Goco8CeeG+bXHrrB24elOj5kyOcApOYu5PiVmwg9zT3T5hZbiWWIKwMW7eZtYArTw2m5ln6ATD0oY6hkJCNoOQliDc5hFlHt6Tsn0kS+UsuubjmtNETnTDbU/wA8WlLzrdxArrwCgbllUutMoQl/u+413apOSvYzSxzicKntEfJUFTSJ9N; criteoVisitorId=90a3138b-fa48-40d2-909f-05df8ed49382; enabled=1; ReturnUrl=https://www.bestbuy.ca/; surveyOptOut=1; AMCVS_D6E638125859683E0A495D2D%40AdobeOrg=1; s_ecid=MCMID%7C58623995158009063400145498744701609412; AMCV_D6E638125859683E0A495D2D%40AdobeOrg=-1303530583%7CMCIDTS%7C18579%7CMCMID%7C58623995158009063400145498744701609412%7CMCAAMLH-1605795384%7C7%7CMCAAMB-1605795384%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1605197784s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0; _fbp=fb.1.1605190584865.1943329646; __gads=ID=b9bf01c0bd787ad3:T=1605190585:S=ALNI_MaebI2g19TYrhP4blFVaZP-OH171w; ak_bmsc=5C893CBEA125A1AE467720D5114D112CB896608D2D380000B843AD5FF451955F~plgYLJkroJOpfNWJ0CO85DqrbAyjQeNT/sQRMMn/JeOUGz3KrEepLFx/PzOB+uCm59Z1LwlXuGNlbs22Inn09EEXwe/Y0mqOt+ZTOGfX0OZ0J6gWRVieAsm3demZg+WViqfB5tIAZhJ27kGcNWIAZOOo9CoqKyPbb1+rzao4EmT4Qin0aZrYlmQJThHpJSQ0we7tzfQr0NxDpGdMxKFwwR5FdxPNyKtpXYxXaNOftLHxZdXcigDKR7iVOhfSr+H+Qe; check=true; dtm_mSession=880c829867f5497f863120e9df5804fd; gbi_visitorId=ckhex12gr00013b8czxg237oe; gbi_sessionId=ckhex12gr00003b8c2c66raua; QueueITAccepted-SDFrts345E-V3_dryrun4b2020browse=EventId%3Ddryrun4b2020browse%26QueueId%3D00000000-0000-0000-0000-000000000000%26RedirectType%3Ddisabled%26IssueTime%3D1605190585%26Hash%3D6f5c481f337210ae57275a81fe52341144b48ded960266f591f39f14b7d5ae3d; _gcl_dc=GCL.1605190585.EAIaIQobChMIlqTN85j97AIVjLbICh3P6g9AEAAYASAAEgKVifD_BwE; _gcl_aw=GCL.1605190585.EAIaIQobChMIlqTN85j97AIVjLbICh3P6g9AEAAYASAAEgKVifD_BwE; _gcl_au=1.1.1982688386.1605190585; _abck=66133E578B7374D6FA7123565DE4F964~0~YAAQjWCWuO931Hd1AQAAfY7QvAR5eMA1Ed9ekSSxNMCucIHthk2iCzHRvS7fMPQas80m3PiS4M1qLTrpCrMtHd0bJpqzQOlbLg4RoQWHHINa24DYY0LZJXEon7hTuXVlavEbZlvqHfrep7fQneV2P35oAo/IBmDdNZcj8bLoOwljlgCsB+c7SQTtmdVOQa3++hQykWT5MwaxVyi+aT2m09zlw5eruMXcGCSLx7Xe0LN90E1OKqp/2IM3P/1eXN6W8az16kxoa+rA7iAaFzouP5Vh7ZTR3+9k+avP7G6AgjHI4I3bvsWyXqeIuqUbcCt35JtUItWeeRjiFFMo4G8aR8QFuu7TIA==~-1~||-1||~-1; s_lv_s=First%20Visit; s_vnum=1606798800553%26vn%3D1; s_invisit=true; s_ev46=%5B%5B%27knc-c-71700000055463805-k-43700045995118730%27%2C%271605190585554%27%5D%5D; AA_previousTA=; s_cc=true; _pin_unauth=dWlkPU1HSTFOV0ppWlRndFpESmxPUzAwWXpZMExUaGhNelV0T1RBeU1tWXpZV1poWmpCaA; _ga=GA1.2.237646344.1605190585; _gid=GA1.2.426164460.1605190586; _gac_UA-122294325-1=1.1605190586.EAIaIQobChMIlqTN85j97AIVjLbICh3P6g9AEAAYASAAEgKVifD_BwE; BVBRANDSID=9a5017eb-374d-410e-b9f4-21a2b85207ab; BVBRANDID=409021b4-6c0d-427f-b6a7-64a47af67eb1; BVImplmain_site=18193; nps={"currentUrlPath":"/en-ca/basket","hasSurveyBeenDisplayed":false,"heartBeat":1605190606,"isInSampling":false,"pageViewCount":4,"surveyLastDisplayed":1636726584}; tx=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjYzVlMGMxMS02OWRkLTRkODEtODJkYy1kZjNjOTBkN2M1NDgifQ.XCXBsAi6fmEFKAhTVSR-NaQ9n4zvxfZvmVCn7cUASrk; fdb7491a5cc3d693edd0926b3a48659f=5d3ea0bea86b891dd0733d81d50f43f1; AA_previousPageType=; s_sq=%5B%5BB%5D%5D; rxVisitor=1605190613101UL21U9HRQB9NTF0ACMVBD0UBJICK105N; dtSa=-; dtLatC=4; b6bab32db12a74433294191e1fddb23a=e8115415ae401cc767a8d7764167caa2; _derived_epik=dj0yJnU9OUVWeWc1SHNsWGpoRmxwQTAxSnN1bjQzZlVzU0lJQm8mbj0wOV9GUWpLTHUwNFdSV1Z3N25SWkJ3Jm09NyZ0PUFBQUFBRi10UTlZ; QueueITAccepted-SDFrts345E-V3_dryrun42020checkout=EventId%3Ddryrun42020checkout%26QueueId%3D00000000-0000-0000-0000-000000000000%26RedirectType%3Ddisabled%26IssueTime%3D1605190614%26Hash%3D505f062c3f83fae1418cd4b60131d0f55c0cdc9007098256dbf2641a242d8a3c; 47236a0d189c10314faac13e28785259=aab1bc94a40be7f7ad6b04db3dd5b281; dtPC=1$190613098_142h-vHHBFCQMKPWVSQTCPCPKOAPHTLIHOCNVR-0e1; dtCookie=1$AF855474C4A3AC02F7E959462AD46E95; rxvt=1605192416236|1605190613103; mbox=session#880c829867f5497f863120e9df5804fd#1605192445|PC#880c829867f5497f863120e9df5804fd.35_0#1668435417; AA_hasSeenCheckoutThisVisit=true; AA_pagePathingCount=8; s_lv=1605190616261; s_getNewRepeat=1605190616264-New; AA_previousCategory=dth%20checkout; AA_previousPageName=checkout%20|dth%20checkout%20|shipping; bm_sv=D3A4A3A6F8E7DD27725233C0DE6C1DB2~aqc+xQqxn9n0KPKA2fp97cg7N9i1PDF1uWylk+djsqzPjpTE7T9MUrzOMD67xJDSzwGaLwsTJO7OGNu6HQfYV/0YWDLpAWw5P9rF82bwvAbZmLio+GXuVsYY4MeWq99MPhja9HO7gibKFWmhgz6XWEvMTdveJ/BtjmO3qxeDsc4=; rxVisitor=1605190613101UL21U9HRQB9NTF0ACMVBD0UBJICK105N; ai_session=o7cbENikkFIgg5mSZi6nk8|1605190584530|1605190640202.7; dtCookie=1$AF855474C4A3AC02F7E959462AD46E95; cartId=615d0dae-0c80-4698-8432-7c96b6747954; dtLatC=7; dtPC=1$190613098_142h11vHHBFCQMKPWVSQTCPCPKOAPHTLIHOCNVR-0e1; rxvt=1605192455533|1605190613103'
xtx = 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjYzVlMGMxMS02OWRkLTRkODEtODJkYy1kZjNjOTBkN2M1NDgifQ.XCXBsAi6fmEFKAhTVSR-NaQ9n4zvxfZvmVCn7cUASrk'
####################################################################



class bestbuy:
    def __init__(self,proxy, proxyornot=False, oneonly = True):
        self.oneonly = oneonly
        self.proxy = proxy
        self.session = HTMLSession()
        self.proxyornot = proxyornot
        lineItems = {}
        self.set_cookies()
        print('cookies set')
        while True:
            try:
                lineItems = self.atc()
            except Exception as e:
                print(e)
                pass
            if lineItems[0]["total"] != 0 :
                try:
                    obj = self.submit_shipping(lineItems)
                    id = obj[0]
                    totalPurchasePrice = obj[1]
                    self.submit_payment(id)
                    if self.submit_order(id, totalPurchasePrice) and self.oneonly:
                        break
                    else:
                        pass
                except Exception as e:
                   traceback.print_exc()
                   pass

            # sleep = random.randint(1, 10)
            # print(f"sleep {sleep}")
            # time.sleep(sleep)
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
        response = self.session.get('https://www.bestbuy.ca/en-ca')
        print(response)

    def atc(self):
        add_to_cart_url = "https://www.bestbuy.ca/api/basket/v2/baskets"
        data = {"lineItems":[{"sku":"","quantity":1}]}
        data["lineItems"][0]["sku"] = sku
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-CA",
            "Content-Length":"47",
            "content-type": "application/json",
            "origin": "https://www.bestbuy.ca",
            "postal-code": "H3G",
            "region-code": "QC",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Host": "www.bestbuy.ca",
           #"x-tx": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmNDZjZjE1Ny04N2Q4LTQwZDMtOGQzNy0yYzA3ZjdhMDM3OGUifQ.0oSnniqudGcnuJa67TB2qI6wyid-erEO6BqRCd0YZfo"
        }
        if self.proxyornot:
            r = self.session.post(add_to_cart_url, data=json.dumps(data), headers=headers, proxies=self.proxy)
        else:
            r = self.session.post(add_to_cart_url, data=json.dumps(data), headers=headers)
        print('############')
        print('adding' + sku + ' to cart')
        #print(r.text)
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

    def start_checkout(self):
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-CA",
            "Content-Length": "47",
            "content-type": "application/json",
            "origin": "https://www.bestbuy.ca",
            "postal-code": "H3K",
            "region-code": "QC",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Host": "www.bestbuy.ca"}
        r = self.session.get("https://www.bestbuy.ca/checkout/?qit=1#/en-ca/shipping/", headers=headers)
        print(r.text)
        print(self.session.cookies.get_dict())

    def submit_shipping(self,lineItems):
        data = {"email":"lzweijinwei196@gmail.com","shippingAddress":{"address":"1450, RENÉ-LÉVESQUE BLVD. WEST, 1510","apartmentNumber":""
            ,"city":"montreal","country":"CA","firstName":"ziwei","lastName":"li","phones":[{"ext":"","phone":"4387258504"}]
            ,"postalCode":"H3G0E1","province":"QC"}}
        data["lineItems"] = lineItems
        print(data)

        cookies_str=[]
        base="%s=%s"
        for name, cookie in self.session.cookies.items():
            cookies_str.append(base % (name, cookie))
        cookies_str = '; '.join(cookies_str)

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
            'cookie':cookies_str,
            "x-tx":xtx
        }


        if self.proxyornot:
            r = self.session.post(order_url, headers=shipping_headers, json=data, proxies=self.proxy, cookies=self.session.cookies)
        else:
            r = self.session.post(order_url,headers=shipping_headers,json=data, cookies=self.session.cookies)
        print("#######################")
        print('submit shipping')
        print(r.text)
        id = json.loads(r.text)["id"]
        totalPurchasePrice = json.loads(r.text)["totalPurchasePrice"]
        print('exiting at shipping as this is a test run, find this line and comment out the next line if you want real runs')
        exit(0)
        return [id, totalPurchasePrice]

    def submit_payment(self,id):
        print('############')
        print('submiting payment')
        url = "https://www.bestbuy.ca/api/checkout/checkout/orders/"+id+"/payments"
        data = {"email":"lzweijinwei196@gmail.com",
                "payment":{"creditCard":{"billingAddress":{"address":"1450, RENÉ-LÉVESQUE BLVD. WEST, 1510","apartmentNumber":""
                    ,"city":"montreal","country":"CA","email":"lzweijinwei196@gmail.com","firstName":"ziwei","lastName":"li",
                                                           "phones":[{"ext":"","phone":"4387258504"}],"postalCode":"H3G0E1",
                                                           "province":"QC"},
                                         "cardNumber":"FaWyaCoECrrrkQz4I3O+M4NM+MnNjaa0qywcTR309KfKB1CNbuCpuQOHdd4pjzcvA9LsxStLWMfNTTqoXcXeiO4HLVXXqumXUEEIMXQoSBqj1vDHfaqJKCv1DrF/IU3jJXRQpzfl+TiuIah04LWzeuyohWg4ig2sKY7SyAQi22dFxiiyK71eKYcI0Xp9AOBx1Vrra4SQEjGCCH4PlkCYPsn9LdLR2uJrnRZdx7p5YgK9fXMTndfsmUdLqgCcdhM6hl6A6BjZIhJDd/WzyuiN/1SJy9eQF5KBnSg2s3oNQUxTd/KrXYkv/25ezf2EK4hOu7ds5BVZjgP2VPUHhNQnDg==6631",
                                         "cardType":"VISA","cvv":"187","expirationMonth":"3","expirationYear":"2023"}}}

        headers = {
            "accept": "application/vnd.bestbuy.checkout+json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-CA",
            "content-type": "application/json",
            "content-length": "493",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Host": "www.bestbuy.ca",
            "referer": "https://www.bestbuy.ca/checkout/",
            "x-dtreferer": "https://www.bestbuy.ca/checkout/#/en-ca/shipping/QC/H3G0E1",
            #'cookie': cookie,
            "x-tx": xtx
        }
        if self.proxyornot:
            r = self.session.put(url,headers=headers,json=data, proxies = self.proxy, cookies=self.session.cookies)
        else:
            r = self.session.put(url,headers=headers,json=data, cookies = self.session.cookies)
        print(r.text)

    def submit_order(self,id,totalPurchasePrice):
        url = "https://www.bestbuy.ca/api/checkout/checkout/orders/submit"
        headers = {
            "accept": "application/vnd.bestbuy.checkout+json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-CA",
            "content-type": "application/json",
            "content-length": "493",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Host": "www.bestbuy.ca",
            "referer": "https://www.bestbuy.ca/checkout/",
            # "x-tx": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NjZmNDlmNy01MmNhLTQ5YmQtYTZjZi0wMTA4NzU1MDNlMTUifQ.CsMAVW85JR97WyRgeNLx9nME0cgYIwaLL1n5DvjGepo",
            "x-dtreferer": "https://www.bestbuy.ca/checkout/#/en-ca/shipping/QC/H3G0E1",
            #'cookie': cookie,
            "x-tx": xtx
        }
        data = {"cvv":"187","email":"lzweijinwei196@gmail.com","secureAuthenticationResponse":"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"}
        data["totalPurchasePrice"] = totalPurchasePrice
        data["id"] = id
        if self.proxyornot:
            r = self.session.post(url, headers=headers, json=data, proxies=self.proxy)
        else:
            r = self.session.post(url, headers=headers,json=data)
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

proxies = load_proxy('proxy.text')
while True:
    the_proxy = parse_proxy(random.choice(proxies))
    try:
        #When creating the bestbuy obj, its default to use proxy and only checkout once, u can pass in different params.
        bestbuy = bestbuy(the_proxy)

    except Exception as e:
        print(e)

