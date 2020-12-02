from requests_html import HTMLSession
import json
import datetime
import time
import selenium_wrapper.selenium_support as ss
from util.decorators import *
#link for test
#currently every single call that have been made during the checkout process are established
#stucked at submit payment
#cookie is mandetory, and cookie includes the bucket info. the bucket id wouldnt change under the same cookie.
cookie=\
    'wm.device_fingerprint=abe2de66-1882-414a-b604-eb95bf618062; ENV=ak-scus-t1-prod; vtc=bSPRm6eDVQfnldRP_pBqK0; bstc=bSPRm6eDVQfnldRP_pBqK0; walmart.nearestLatLng="45.4978,-73.5485"; TS017d5bf6=01538efd7c057049440d895e3962e2e4e028cd5193978ad5c0102ea9cf81867d2aa0cf594596c1db8fe823661087a8fa36cade0210; userSegment=40-percent; _ga=GA1.2.1037395997.1606941921; _gid=GA1.2.1630367376.1606941921; dtCookie=-15$B5CV93BIR3SLDH2KR6HBN02ND59L7AGT; enableHTTPS=1; TS01170c9f=01538efd7c057049440d895e3962e2e4e028cd5193978ad5c0102ea9cf81867d2aa0cf594596c1db8fe823661087a8fa36cade0210; deliveryCatchment=3165; defaultNearestStoreId=1170; headerType=whiteGM; xpa=2lwWQ|63K3S|6V3fl|7Xi3l|DViIf|DwTRU|GpBCe|HbOxV|Jeavw|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Q0IHr|X92ox|YJsua|_vY-K|a4vv4|dykD1|fHfTr|fJumS|gknoM|hcz5Y|jeBOs|lZnE7|mOlOu|rwaVg|sGGbM|wM_1h|wx8xe|yI7_k; exp-ck=6V3flk7Xi3l1DwTRU1GpBCe1HbOxV1Jeavw1MZ9tt1Oqgc14X92ox4YJsua5a4vv41dykD11fHfTr2fJumS3gknoM1lZnE76rwaVg4sGGbM4wM_1h1wx8xe1yI7_k1; dtSa=true%7CKU13%7C-1%7Csearch-form-input%7C-%7C1606941934181%7C140007527_877%7Chttps%3A%2F%2Fwww.walmart.ca%2Fen%2Felectronics%2Ftv-video%2Ftvs%2FN-1170%7CSmart%20TVs%20%26%204K%20TVs%20%5Ep%20Walmart%20Canada%7C1606940009315%7C%7C; rxVisitor=1606941934656D219GJPLE6IIMSPJGEOERL5LRT5A58KF; rxvt=1606943734659|1606941934110; dtPC=-15$140007527_877h-vLDLSAHLITHUUVRETWPULPDGXMMISHPWS-0; xpm=1%2B1606941934%2BbSPRm6eDVQfnldRP_pBqK0~%2B0; walmart.id=46471315-e7ea-409a-8f2d-9a9f8a12479d; _pxvid=53c0d619-34df-11eb-b7fd-0242ac12000f; DYN_USER_ID=e4ed88ed-8e21-479b-adf2-b7a1799f9c8d; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4sVk+xW/e7jsEOzjcaycqJci5rEECYqcbdNzRlsrIxdBIthcYFWHd7PekT5aZ0w/eo+f/tHxDHw7bn2/R3/+G+3BUpYsDT0wtPj2nEG7Y+Dm7rww66Q8cUDNyc/3DSOaxj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0NFwCnXZbVdyvUnjgDUgmFoCkOKZF7Z5AORB7s6J6jiRkEtqKG5Hd0rU8WMUVKk6fb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEGeGBzYKYyrDIu+dUAqgHHxJJ30qDmjUartcsuV4Zslw2IIlEVtk6G82CYT5BZrpX1+DwN7yJ154Qy2cXb3IFrC4JlBTKFcqqp7w7wbz0zmIifzg5XYqAwk+fencKlCIYg==; LT=1606941935271; _gcl_au=1.1.1965568082.1606941935; _fbp=fb.1.1606941935266.1387734787; s_vi=[CS]v1|2FE3FE778515F0AD-60000AEFEDDA537F[CE]; s_ecid=MCMID%7C41461621577161284753197488739699308874; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; s_visit=1; __gads=ID=75b93ff892648bd5-2241613772b800eb:T=1606941935:S=ALNI_MYsbExYB2GoIAPkKT6csme83D_AqQ; s_cc=true; AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18599%7CMCMID%7C41461621577161284753197488739699308874%7CMCAID%7C2FE3FE778515F0AD-60000AEFEDDA537F%7CMCOPTOUT-1606949135s%7CNONE%7CMCAAMLH-1607546735%7C7%7CMCAAMB-1607546735%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18606%7CvVersion%7C5.0.1; wmt.c=0; NEXT_GEN.ENABLED=1; cartId=89af9e5d-79f3-4113-a68c-f443eb6ca504; og_session_id=af0a84f8847311e3b233bc764e1107f2.670468.1606941965; og_session_id_conf=af0a84f8847311e3b233bc764e1107f2.670468.1606941965; _scid=d2424f47-de6e-4c0d-9708-e3a49bfee626; _pin_unauth=dWlkPVpESXlNREF6WmpVdE1qWmpPUzAwWWpCbExXRTROVGN0Tm1Nd09HSTROR0kyTkdKbA; _sctr=1|1606885200000; localStoreInfo=eyJwb3N0YWxDb2RlIjoiSDNBMk40IiwibG9jYWxTdG9yZUlkIjoiMTE3MCIsInNlbGVjdGVkU3RvcmVJZCI6IjExNzAiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkP0dGUtZGVzLU5laWdlcyBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjMxNjUiLCJmdWxmaWxsbWVudFR5cGUiOiJERUxJVkVSWSJ9; walmart.shippingPostalCode=H3A2N4; walmart.nearestPostalCode=H3A2N4; WM.USER_STATE=GUEST|Guest; _gat=1; _px3=52b5cb3220d560c9898ff351f2b6f8dc92f234ccb783b27047f0d027d626d860:x2Gb2EJf/h3WN1pna1G/GtmtJDgJSpAhDjSOPwy40quQz0o3Y76s2QkBQX1XvdlDCECsMglfqlZvULfefnCnUw==:1000:/7Tv0tRqPXW/kcsiWxDuilAoUMCq7E0K4yFeMdgl7THPmcZTw3laHnybPW8t7srUwJLOats/YOfAd6P8LPoKA8hrEFz8Ghez0W76jBT9O+nYHWwgXYPdBNPLQ8sqKkHtbPIgVB6MS6YRkp+s6i1egNXagy1ysotolI7o/Tl+ssw=; _pxde=e7abc3e4e3856aa17f4eb991cbc9ea48f1f9ea1e32639876d11cf50d8aea2529:eyJ0aW1lc3RhbXAiOjE2MDY5NDMyNjI3MDgsImZfa2IiOjAsImlwY19pZCI6W119; s_gnr=1606943264953-New; _uetsid=65bc062034df11eb9699b51359aeeb7a; _uetvid=65bc35c034df11ebac95b995ec776293; authDuration={"lat":"1606943266574000","lt":"1606943266574000"}; TS0196c61b=01538efd7c5da905745daf29b3712fdbe0f9e12e1e80ea651350dd5482b28969971ea232c24c5e4a03f78a00639f114dfc1b729822; cto_bundle=LfCBrV9rcnclMkJSTTNJNjJPN2pWUDhCSm5Vb3VqanB2eW5lJTJCJTJGS3RvTGIwMVJXVmRJZlFBSGs2d2lqU3NtT3RjNUElMkJGUk9ld1ljUmJhZ2hLN1NrWUJoUVh6aGZ1YThXR2tDR1JPanNqZHphd0pWQVZaYjJGVHR6ZzA2c3JTR2Q4SzFxUzlVbU1oVnZJWjVPNFVTeUt0ejhaUENCUSUzRCUzRA; seqnum=114; akavpau_ca_prod_akamai_vp=1606943567~id=886eb5693055c6a56ee3c7b10a9d6542; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DCheckout%2526link%253DNext%2526region%253Dstep1%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DCheckout%2526pidt%253D1%2526oid%253DNext%2526oidt%253D3%2526ot%253DSUBMIT'
product_link = 'https://www.walmart.ca/en/ip/paw-patrol-dino-rescue-chases-deluxe-rev-up-vehicle/6000201418461'
header = {
    'origin': 'https://www.walmart.ca',
    'referer': 'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    #'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=whiteGM; ENV=ak-dfw-prod; vtc=SSsOobpNazV42hodX3uuDg; bstc=SSsOobpNazV42hodX3uuDg; walmart.nearestPostalCode=H3C9Z0; walmart.nearestLatLng="45.4978,-73.5485"; TS01f4281b=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; TS011fb5f6=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; userSegment=40-percent; akavpau_CA_PROD_Product_page=1604796507~id=5f6b304d625b8759b3cfd88ebf6825ad; walmart.id=09fa06f1-d48f-4331-b304-962351628d00; s_gnr=1604796207581-New; xpa=2lwWQ|2oqzF|63K3S|6V3fl|6iOkF|6rNcs|7Xi3l|DwTRU|GpBCe|HbOxV|IJ4rZ|Jeavw|KpQ33|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Pic8m|Q0IHr|SIe2y|SNvE3|VIGCY|X92ox|XBdGQ|YJsua|YcwI-|YxLOx|_vY-K|a4vv4|biw7H|c8ThE|fJumS|hcz5Y|jeBOs|kZ1Eq|lZnE7|mOlOu|o5Sri|pldE2|rwaVg|sGGbM|wx8xe|yI7_k; exp-ck=2oqzF26V3flk6iOkF46rNcs27Xi3l1DwTRU1GpBCe1HbOxV1IJ4rZ1Jeavw1KpQ334MZ9tt1Oqgc14Pic8m1SIe2y1SNvE31X92ox4XBdGQ1YJsua5YcwI-1YxLOx1a4vv41c8ThE1fJumS3kZ1Eq1lZnE76o5SribpldE21rwaVg4sGGbM4wx8xe1yI7_k1; TS0175e29f=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; _ga=GA1.2.621116102.1604796208; _gid=GA1.2.277603389.1604796208; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; _pxvid=6a906779-215b-11eb-8b2e-0242ac120002; DYN_USER_ID=67580559-be36-433f-a489-d98e44ea4b96; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4lE3R78tOCzf5oqjeoCyS3H05m3hzgaXwN1STznaWKE+/mQ3ile+7ssKnyiqLFfns+k1ywS8xE58mi/5ybksWpR+KS5BlQpMa1nos97k2sq7bYQCy774TUE5mrXNmprrzj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0lJlHL978H9Z5PKnKHwe8GPtPC56OL433Dk+vTttmq2eHdBtPrB6vbl/Zh6XkbcFHb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEHIMdpRi0iatb7S4HHlAgSoDZHQljs/cWHM0t1Ac18CxDtPMgO/gEqQaSRxkCKFtv7TF0cSrJ9/5larmnocIcWafIZ3T1gAXYw2ULyTQuSCQP44VNKds/cuTqqP7xb674A==; LT=1604796207945; authDuration={"lat":"1604796207852000","lt":"1604796207852000"}; WM.USER_STATE=GUEST|Guest; _fbp=fb.1.1604796207799.1827601776; s_visit=1; s_cc=true; _gcl_au=1.1.376722026.1604796208; xpm=1%2B1604796207%2BSSsOobpNazV42hodX3uuDg~%2B0; _gat=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18575%7CMCMID%7C35491274262018340851842861422459610209%7CMCAAMLH-1605401007%7C7%7CMCAAMB-1605401007%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1604803407s%7CNONE%7CMCSYNCSOP%7C411-18582%7CvVersion%7C5.0.1; __gads=ID=fb9b8a7b64e01c7e:T=1604796208:S=ALNI_MZYXcI7TCkbwPa0hlOS7alB-q3gcQ; _px3=af71a633e7b2ee722cbd963406710d9ab65ebe89e3e5eef22895febad5ed44ce:8dGoVgrzKXh2ayoQXGisuu1DFJBAyTC/3Y+d7XTzGWAaD7Q5phhHMd3gK876tAl/f1B2Vn1rxBtVgR9J/9caFA==:1000:AJBZpuU0vmOqTBiOMqTji8X0oc0RzHwHTS0oYTeVmSoMGEGx4LtzLlUASGPcKkOwq9uSMPuhyVvLs1L8NfsbJCMoqndD9WdpOwBfnQnHpjhB+7f/hotZT7Hhk0nLzKCekKVa0htU1AGz7hdi/k9HUPF7tpaOtGeyuhToXu+PVzI=; _pxde=4fd08518febfb1da764254d1f8a6b478c879e410da997e4516baf52691b0d2c2:eyJ0aW1lc3RhbXAiOjE2MDQ3OTYyMDk4MDYsImZfa2IiOjAsImlwY19pZCI6W119; seqnum=6; akavpau_CA_PROD_Entire_Site=1604796510~id=ffffd7b4cf3f011ae0165079fd029856; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526link%253DAdd%252520to%252520cart%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526pidt%253D1%2526oid%253Dfunctionmr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
    'wm_qos.correlation_id': '4a005237-026-175a54ed043916,4a005237-026-175a54ed043fdb,4a005237-026-175a54ed043fdb'
}


class Walmart:
    @debug
    def __init__(self):
        self.session = HTMLSession()
        self.set_cookies()
        #exit(0)
        self.session.get(product_link)
        self.atc()
        self.shipping()

    @debug
    def set_cookies(self):
        crawler = ss.Walmart('../chromedriver.exe', headless=True)
        crawler.login()
        cookies = crawler.browser.get_cookies()
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
        data = {"postalCode":"H3S2B2","items":[{"offerId":"6000201418464","skuId":"6000201418464","quantity":1,"allowSubstitutions":True,"subscription":False,"action":"ADD","availabilityStoreId":"3165","pricingStoreId":"1170"}],"pricingStoreId":"1170"}
        r = self.session.post(link, headers=header, json=data)
        print(r.text)

    @debug
    def shipping(self):
        #initate checkout
        r_start = self.session.get('https://www.walmart.ca/api/checkout-page/checkout?lang=en&availStoreId=3165&postalCode=H3G0E1', headers=header)
        #links
        link = 'https://www.walmart.ca/api/checkout-page/checkout/email?availStore=3165&postalCode=H3A2N4'
        shipping_link = 'https://www.walmart.ca/api/checkout-page/checkout/address?lang=en&availStore=3165&slotBooked=false'
        postal_link = 'https://www.walmart.ca/api/checkout-page/edd?postalCode=H3G0E1'
        summary_link ='https://www.walmart.ca/api/checkout-page/payments/summaryhttps://www.walmart.ca/api/checkout-page/payments/summary'
        ###########################################################
        email_data = '{"emailAddress":"lzwei196@163.com"}'
        shipping_data = '{"fulfillmentType":"SHIPTOHOME","deliveryInfo":{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G0E1","phone":"4387258504","saveToProfile":true,"country":"CA","locationId":null,"overrideAddressVerification":false}}'
        postal_data = '{"order":{"subTotal":147,"fulfillmentType":"SHIPTOHOME","isPOBoxAddress":false},"sellers":[{"sellerId":"0","itemTotal":147,"items":[{"skuId":"6000197280859","offerId":"6000197280859","quantity":1,"shipping":{"options":["STANDARD"],"type":"PARCEL","isShipAlone":false},"isDigitalItem":false,"isFreightItem":false}]}]}'
        #data = {"fulfillmentType":"SHIPTOHOME","deliveryInfo":{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G 0E1","phone":"4387258504","saveToProfile":'true',"country":"CA","locationId":'null',"overrideAddressVerification":'false'}}
        summary_data = '{"orderTotal":29.79,"paymentMethods":[{"piHash":{"pan":"4520028185626631","cvv":"217","encryption":{"integrityCheck":"fcf90fff8e7d0c5e","phase":"1","keyId":"b73eb61c"}},"cardType":"CREDIT_CARD","pmId":"VISA","cardLast4Digits":"6631","referenceId":"pkeurr"}]}'
        r_email= self.session.post(link, headers=header, json=email_data)
        r_shipping = self.session.post(shipping_link, headers=header, json=shipping_data)
       # r_postal = self.session.post(postal_link, headers=header, json=postal_data)
        r_summary = self.session.post(summary_link, headers=header, json=summary_data)
        #print(r_summary.text)

walmart = Walmart()