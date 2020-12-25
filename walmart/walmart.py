from requests_html import HTMLSession
import json
import datetime
import time
from pprint import  pprint
import selenium_wrapper.selenium_support as ss
from util.decorators import *
from util.request_bot import Requests_bot
#link for test
#currently every single call that have been made during the checkout process are established
#stucked at submit payment
#cookie is mandetory, and cookie includes the bucket info. the bucket id wouldnt change under the same cookie.
email = 'lzwei196@163.com'
first ='ziwei'
last = 'li'

product_link = 'https://www.walmart.ca/en/ip/paw-patrol-dino-rescue-chases-deluxe-rev-up-vehicle/6000201418461'
header = {
    'origin': 'https://www.walmart.ca',
    'referer': 'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    #'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=whiteGM; ENV=ak-dfw-prod; vtc=SSsOobpNazV42hodX3uuDg; bstc=SSsOobpNazV42hodX3uuDg; walmart.nearestPostalCode=H3C9Z0; walmart.nearestLatLng="45.4978,-73.5485"; TS01f4281b=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; TS011fb5f6=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; userSegment=40-percent; akavpau_CA_PROD_Product_page=1604796507~id=5f6b304d625b8759b3cfd88ebf6825ad; walmart.id=09fa06f1-d48f-4331-b304-962351628d00; s_gnr=1604796207581-New; xpa=2lwWQ|2oqzF|63K3S|6V3fl|6iOkF|6rNcs|7Xi3l|DwTRU|GpBCe|HbOxV|IJ4rZ|Jeavw|KpQ33|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Pic8m|Q0IHr|SIe2y|SNvE3|VIGCY|X92ox|XBdGQ|YJsua|YcwI-|YxLOx|_vY-K|a4vv4|biw7H|c8ThE|fJumS|hcz5Y|jeBOs|kZ1Eq|lZnE7|mOlOu|o5Sri|pldE2|rwaVg|sGGbM|wx8xe|yI7_k; exp-ck=2oqzF26V3flk6iOkF46rNcs27Xi3l1DwTRU1GpBCe1HbOxV1IJ4rZ1Jeavw1KpQ334MZ9tt1Oqgc14Pic8m1SIe2y1SNvE31X92ox4XBdGQ1YJsua5YcwI-1YxLOx1a4vv41c8ThE1fJumS3kZ1Eq1lZnE76o5SribpldE21rwaVg4sGGbM4wx8xe1yI7_k1; TS0175e29f=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; _ga=GA1.2.621116102.1604796208; _gid=GA1.2.277603389.1604796208; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; _pxvid=6a906779-215b-11eb-8b2e-0242ac120002; DYN_USER_ID=67580559-be36-433f-a489-d98e44ea4b96; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4lE3R78tOCzf5oqjeoCyS3H05m3hzgaXwN1STznaWKE+/mQ3ile+7ssKnyiqLFfns+k1ywS8xE58mi/5ybksWpR+KS5BlQpMa1nos97k2sq7bYQCy774TUE5mrXNmprrzj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0lJlHL978H9Z5PKnKHwe8GPtPC56OL433Dk+vTttmq2eHdBtPrB6vbl/Zh6XkbcFHb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEHIMdpRi0iatb7S4HHlAgSoDZHQljs/cWHM0t1Ac18CxDtPMgO/gEqQaSRxkCKFtv7TF0cSrJ9/5larmnocIcWafIZ3T1gAXYw2ULyTQuSCQP44VNKds/cuTqqP7xb674A==; LT=1604796207945; authDuration={"lat":"1604796207852000","lt":"1604796207852000"}; WM.USER_STATE=GUEST|Guest; _fbp=fb.1.1604796207799.1827601776; s_visit=1; s_cc=true; _gcl_au=1.1.376722026.1604796208; xpm=1%2B1604796207%2BSSsOobpNazV42hodX3uuDg~%2B0; _gat=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18575%7CMCMID%7C35491274262018340851842861422459610209%7CMCAAMLH-1605401007%7C7%7CMCAAMB-1605401007%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1604803407s%7CNONE%7CMCSYNCSOP%7C411-18582%7CvVersion%7C5.0.1; __gads=ID=fb9b8a7b64e01c7e:T=1604796208:S=ALNI_MZYXcI7TCkbwPa0hlOS7alB-q3gcQ; _px3=af71a633e7b2ee722cbd963406710d9ab65ebe89e3e5eef22895febad5ed44ce:8dGoVgrzKXh2ayoQXGisuu1DFJBAyTC/3Y+d7XTzGWAaD7Q5phhHMd3gK876tAl/f1B2Vn1rxBtVgR9J/9caFA==:1000:AJBZpuU0vmOqTBiOMqTji8X0oc0RzHwHTS0oYTeVmSoMGEGx4LtzLlUASGPcKkOwq9uSMPuhyVvLs1L8NfsbJCMoqndD9WdpOwBfnQnHpjhB+7f/hotZT7Hhk0nLzKCekKVa0htU1AGz7hdi/k9HUPF7tpaOtGeyuhToXu+PVzI=; _pxde=4fd08518febfb1da764254d1f8a6b478c879e410da997e4516baf52691b0d2c2:eyJ0aW1lc3RhbXAiOjE2MDQ3OTYyMDk4MDYsImZfa2IiOjAsImlwY19pZCI6W119; seqnum=6; akavpau_CA_PROD_Entire_Site=1604796510~id=ffffd7b4cf3f011ae0165079fd029856; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526link%253DAdd%252520to%252520cart%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526pidt%253D1%2526oid%253Dfunctionmr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
    #'wm_qos.correlation_id': '4a005237-026-175a54ed043916,4a005237-026-175a54ed043fdb,4a005237-026-175a54ed043fdb'
}

TIMOUT=15
class Walmart(Requests_bot):
    @debug
    def __init__(self):
        super(Walmart, self).__init__(TIMEOUT=TIMOUT)
        self.session = HTMLSession()
        self.set_cookies()
        #exit(0)
        self.session.get(product_link)
        self.atc()
        self.shipping()

    @debug
    def set_cookies(self):
        self.crawler = ss.Walmart('../chromedriver.exe', headless=True)
        self.crawler.login()
        self.crawler.visit_site('https://www.walmart.ca/checkout')
        time.sleep(10)
        cookies = self.crawler.browser.get_cookies()
        for cookie in cookies:
            self.session.cookies.set(cookie['name'], cookie['value'])


    @debug
    def atc(self):
        link = 'https://www.walmart.ca/api/product-page/v2/cart?responseGroup=essential&storeId=3165&lang=en'
        header = {
            'origin':'https://www.walmart.ca',
            #'referer':'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'content-type':'application/json',
            'accept':'application/json',
            #'wm_qos.correlation_id':'4a005237-026-175a54ed043916,4a005237-026-175a54ed043fdb,4a005237-026-175a54ed043fdb'
        }
        data = {"postalCode":"H3S2B2","items":[{"offerId":"6000201418464", "skuId":"6000201418464","quantity":1,"allowSubstitutions":True,"subscription":False,"action":"ADD","availabilityStoreId":"3165","pricingStoreId":"1170"}],"pricingStoreId":"1170"}
        r = self.post(link, headers=header, json=data)

    @debug
    def shipping(self):
        #self.pre_shipping()
        #initate checkout
        r_start = self.get('https://www.walmart.ca/api/checkout-page/checkout?lang=en&availStoreId=3165&postalCode=H3G0E1', headers=header)
        #links
        email_link = 'https://www.walmart.ca/api/checkout-page/checkout/email?availStore=3165&postalCode=H3G0E1'
        shipping_link = 'https://www.walmart.ca/api/checkout-page/checkout/address?lang=en&availStore=3165&slotBooked=false'
        summary_link ='https://www.walmart.ca/api/checkout-page/payments/summary'
        place_order = 'https://www.walmart.ca/api/checkout-page/checkout/place-order?lang=en&availStoreId=1061&postalCode=H3G0E1'
        ###########################################################
        email_data = {"emailAddress":email}
        r_email = self.post(email_link, headers=header, json=email_data)
        print('email', r_email, r_email.text)
        shipping_data = {"fulfillmentType":"SHIPTOHOME","deliveryInfo":{"firstName":first,"lastName":last,"addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G0E1","phone":"4387258504","saveToProfile":'true',"country":"CA","locationId":None,"overrideAddressVerification":'false'}}
        r_shipping = self.post(shipping_link,  json=shipping_data)
        print('shipping',r_shipping, r_shipping.text)
        price = r_email.json()['orderPriceInfo']["total"]
        #postal_data = '{"order":{"subTotal":147,"fulfillmentType":"SHIPTOHOME","isPOBoxAddress":false},"sellers":[{"sellerId":"0","itemTotal":147,"items":[{"skuId":"6000197280859","offerId":"6000197280859","quantity":1,"shipping":{"options":["STANDARD"],"type":"PARCEL","isShipAlone":false},"isDigitalItem":false,"isFreightItem":false}]}]}'
        #data = {"fulfillmentType":"SHIPTOHOME","deliveryInfo":{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G 0E1","phone":"4387258504","saveToProfile":'true',"country":"CA","locationId":'null',"overrideAddressVerification":'false'}}
        summary_data = {"orderTotal":price,"paymentMethods":[{"piHash":{"pan":"4520028185626631","cvv":"217","encryption":{"integrityCheck":"fcf90fff8e7d0c5e","phase":"1","keyId":"b73eb61c"}},"cardType":"CREDIT_CARD","pmId":"VISA","cardLast4Digits":"6631","referenceId":"pkeurr"}]}
        r_summary = self.post(summary_link, json=summary_data)
        print(r_summary, r_summary.text)
        place_order_data = {"cvv":[{"credentialEncrypted":True,"paymentId":"f1e31d7c-9e93-4e8b-af46-69df45a508bf","voltageCredential":{"cypherTextCvv":"125","cypherTextPan":"4724094024082919","integrityCheck":"8abb4194ad94f7ea","keyId":"a2cd8300","phase":1}}],"ogInfo":{"ogSessionId":"af0a84f8847311e3b233bc764e1107f2.146933.1606956588","ogAutoship":False}}
        r_place = self.post(place_order, json=place_order_data)
        print(r_place, r_place.text)

walmart = Walmart()