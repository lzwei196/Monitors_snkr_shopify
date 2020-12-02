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


product_link = 'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858'
header = {
    'origin': 'https://www.walmart.ca',
    'referer': 'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=whiteGM; ENV=ak-dfw-prod; vtc=SSsOobpNazV42hodX3uuDg; bstc=SSsOobpNazV42hodX3uuDg; walmart.nearestPostalCode=H3C9Z0; walmart.nearestLatLng="45.4978,-73.5485"; TS01f4281b=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; TS011fb5f6=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; userSegment=40-percent; akavpau_CA_PROD_Product_page=1604796507~id=5f6b304d625b8759b3cfd88ebf6825ad; walmart.id=09fa06f1-d48f-4331-b304-962351628d00; s_gnr=1604796207581-New; xpa=2lwWQ|2oqzF|63K3S|6V3fl|6iOkF|6rNcs|7Xi3l|DwTRU|GpBCe|HbOxV|IJ4rZ|Jeavw|KpQ33|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Pic8m|Q0IHr|SIe2y|SNvE3|VIGCY|X92ox|XBdGQ|YJsua|YcwI-|YxLOx|_vY-K|a4vv4|biw7H|c8ThE|fJumS|hcz5Y|jeBOs|kZ1Eq|lZnE7|mOlOu|o5Sri|pldE2|rwaVg|sGGbM|wx8xe|yI7_k; exp-ck=2oqzF26V3flk6iOkF46rNcs27Xi3l1DwTRU1GpBCe1HbOxV1IJ4rZ1Jeavw1KpQ334MZ9tt1Oqgc14Pic8m1SIe2y1SNvE31X92ox4XBdGQ1YJsua5YcwI-1YxLOx1a4vv41c8ThE1fJumS3kZ1Eq1lZnE76o5SribpldE21rwaVg4sGGbM4wx8xe1yI7_k1; TS0175e29f=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; _ga=GA1.2.621116102.1604796208; _gid=GA1.2.277603389.1604796208; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; _pxvid=6a906779-215b-11eb-8b2e-0242ac120002; DYN_USER_ID=67580559-be36-433f-a489-d98e44ea4b96; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4lE3R78tOCzf5oqjeoCyS3H05m3hzgaXwN1STznaWKE+/mQ3ile+7ssKnyiqLFfns+k1ywS8xE58mi/5ybksWpR+KS5BlQpMa1nos97k2sq7bYQCy774TUE5mrXNmprrzj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0lJlHL978H9Z5PKnKHwe8GPtPC56OL433Dk+vTttmq2eHdBtPrB6vbl/Zh6XkbcFHb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEHIMdpRi0iatb7S4HHlAgSoDZHQljs/cWHM0t1Ac18CxDtPMgO/gEqQaSRxkCKFtv7TF0cSrJ9/5larmnocIcWafIZ3T1gAXYw2ULyTQuSCQP44VNKds/cuTqqP7xb674A==; LT=1604796207945; authDuration={"lat":"1604796207852000","lt":"1604796207852000"}; WM.USER_STATE=GUEST|Guest; _fbp=fb.1.1604796207799.1827601776; s_visit=1; s_cc=true; _gcl_au=1.1.376722026.1604796208; xpm=1%2B1604796207%2BSSsOobpNazV42hodX3uuDg~%2B0; _gat=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18575%7CMCMID%7C35491274262018340851842861422459610209%7CMCAAMLH-1605401007%7C7%7CMCAAMB-1605401007%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1604803407s%7CNONE%7CMCSYNCSOP%7C411-18582%7CvVersion%7C5.0.1; __gads=ID=fb9b8a7b64e01c7e:T=1604796208:S=ALNI_MZYXcI7TCkbwPa0hlOS7alB-q3gcQ; _px3=af71a633e7b2ee722cbd963406710d9ab65ebe89e3e5eef22895febad5ed44ce:8dGoVgrzKXh2ayoQXGisuu1DFJBAyTC/3Y+d7XTzGWAaD7Q5phhHMd3gK876tAl/f1B2Vn1rxBtVgR9J/9caFA==:1000:AJBZpuU0vmOqTBiOMqTji8X0oc0RzHwHTS0oYTeVmSoMGEGx4LtzLlUASGPcKkOwq9uSMPuhyVvLs1L8NfsbJCMoqndD9WdpOwBfnQnHpjhB+7f/hotZT7Hhk0nLzKCekKVa0htU1AGz7hdi/k9HUPF7tpaOtGeyuhToXu+PVzI=; _pxde=4fd08518febfb1da764254d1f8a6b478c879e410da997e4516baf52691b0d2c2:eyJ0aW1lc3RhbXAiOjE2MDQ3OTYyMDk4MDYsImZfa2IiOjAsImlwY19pZCI6W119; seqnum=6; akavpau_CA_PROD_Entire_Site=1604796510~id=ffffd7b4cf3f011ae0165079fd029856; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526link%253DAdd%252520to%252520cart%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526pidt%253D1%2526oid%253Dfunctionmr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
    'wm_qos.correlation_id': '4a005237-026-175a54ed043916,4a005237-026-175a54ed043fdb,4a005237-026-175a54ed043fdb'
}


class Walmart:
    @debug
    def __init__(self):
        self.session = HTMLSession()
        self.set_cookies()
        exit(0)
        self.session.get(product_link)
        #self.atc()
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

        link = 'https://www.walmart.ca/api/product-page/v2/cart?responseGroup=essential&storeId=1061&lang=en'
        header = {
            'origin':'https://www.walmart.ca',
            'referer':'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'content-type':'application/json',
            'accept':'application/json',
            'cookie':'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=whiteGM; ENV=ak-dfw-prod; vtc=SSsOobpNazV42hodX3uuDg; bstc=SSsOobpNazV42hodX3uuDg; walmart.nearestPostalCode=H3C9Z0; walmart.nearestLatLng="45.4978,-73.5485"; TS01f4281b=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; TS011fb5f6=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; userSegment=40-percent; akavpau_CA_PROD_Product_page=1604796507~id=5f6b304d625b8759b3cfd88ebf6825ad; walmart.id=09fa06f1-d48f-4331-b304-962351628d00; s_gnr=1604796207581-New; xpa=2lwWQ|2oqzF|63K3S|6V3fl|6iOkF|6rNcs|7Xi3l|DwTRU|GpBCe|HbOxV|IJ4rZ|Jeavw|KpQ33|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Pic8m|Q0IHr|SIe2y|SNvE3|VIGCY|X92ox|XBdGQ|YJsua|YcwI-|YxLOx|_vY-K|a4vv4|biw7H|c8ThE|fJumS|hcz5Y|jeBOs|kZ1Eq|lZnE7|mOlOu|o5Sri|pldE2|rwaVg|sGGbM|wx8xe|yI7_k; exp-ck=2oqzF26V3flk6iOkF46rNcs27Xi3l1DwTRU1GpBCe1HbOxV1IJ4rZ1Jeavw1KpQ334MZ9tt1Oqgc14Pic8m1SIe2y1SNvE31X92ox4XBdGQ1YJsua5YcwI-1YxLOx1a4vv41c8ThE1fJumS3kZ1Eq1lZnE76o5SribpldE21rwaVg4sGGbM4wx8xe1yI7_k1; TS0175e29f=0130aff232a0f84624236526a74d2efdf8dd665b43238f9615647c535a6ec626c3514cecf7c2910cdc92625e7e6d5d33d9eee8e255; _ga=GA1.2.621116102.1604796208; _gid=GA1.2.277603389.1604796208; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; _pxvid=6a906779-215b-11eb-8b2e-0242ac120002; DYN_USER_ID=67580559-be36-433f-a489-d98e44ea4b96; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4lE3R78tOCzf5oqjeoCyS3H05m3hzgaXwN1STznaWKE+/mQ3ile+7ssKnyiqLFfns+k1ywS8xE58mi/5ybksWpR+KS5BlQpMa1nos97k2sq7bYQCy774TUE5mrXNmprrzj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0lJlHL978H9Z5PKnKHwe8GPtPC56OL433Dk+vTttmq2eHdBtPrB6vbl/Zh6XkbcFHb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEHIMdpRi0iatb7S4HHlAgSoDZHQljs/cWHM0t1Ac18CxDtPMgO/gEqQaSRxkCKFtv7TF0cSrJ9/5larmnocIcWafIZ3T1gAXYw2ULyTQuSCQP44VNKds/cuTqqP7xb674A==; LT=1604796207945; authDuration={"lat":"1604796207852000","lt":"1604796207852000"}; WM.USER_STATE=GUEST|Guest; _fbp=fb.1.1604796207799.1827601776; s_visit=1; s_cc=true; _gcl_au=1.1.376722026.1604796208; xpm=1%2B1604796207%2BSSsOobpNazV42hodX3uuDg~%2B0; _gat=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18575%7CMCMID%7C35491274262018340851842861422459610209%7CMCAAMLH-1605401007%7C7%7CMCAAMB-1605401007%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1604803407s%7CNONE%7CMCSYNCSOP%7C411-18582%7CvVersion%7C5.0.1; __gads=ID=fb9b8a7b64e01c7e:T=1604796208:S=ALNI_MZYXcI7TCkbwPa0hlOS7alB-q3gcQ; _px3=af71a633e7b2ee722cbd963406710d9ab65ebe89e3e5eef22895febad5ed44ce:8dGoVgrzKXh2ayoQXGisuu1DFJBAyTC/3Y+d7XTzGWAaD7Q5phhHMd3gK876tAl/f1B2Vn1rxBtVgR9J/9caFA==:1000:AJBZpuU0vmOqTBiOMqTji8X0oc0RzHwHTS0oYTeVmSoMGEGx4LtzLlUASGPcKkOwq9uSMPuhyVvLs1L8NfsbJCMoqndD9WdpOwBfnQnHpjhB+7f/hotZT7Hhk0nLzKCekKVa0htU1AGz7hdi/k9HUPF7tpaOtGeyuhToXu+PVzI=; _pxde=4fd08518febfb1da764254d1f8a6b478c879e410da997e4516baf52691b0d2c2:eyJ0aW1lc3RhbXAiOjE2MDQ3OTYyMDk4MDYsImZfa2IiOjAsImlwY19pZCI6W119; seqnum=6; akavpau_CA_PROD_Entire_Site=1604796510~id=ffffd7b4cf3f011ae0165079fd029856; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526link%253DAdd%252520to%252520cart%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DProduct%25253ARCA%25252032%252522%252520LED%252520HD%252520TV%2526pidt%253D1%2526oid%253Dfunctionmr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
            'wm_qos.correlation_id':'4a005237-026-175a54ed043916,4a005237-026-175a54ed043fdb,4a005237-026-175a54ed043fdb'
        }
        data = {"postalCode":"L5V2N6","items":[{"offerId":"6000197280859","skuId":"6000197280859","quantity":1,"allowSubstitutions":'false',"subscription":'false',"action":"ADD","availabilityStoreId":"1061","pricingStoreId":"1061"}],"pricingStoreId":"1061"}
        r = self.session.post(link, headers=header, json=data)
        print(r.text)

    @debug
    def shipping(self):
        header = {
            'origin': 'https://www.walmart.ca',
            'referer': 'https://www.walmart.ca/en/ip/rca-32-led-hd-tv/6000197280858',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'content-type': 'application/json',
            'accept': 'application/json',
            'cookie':'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=whiteGM; vtc=SSsOobpNazV42hodX3uuDg; userSegment=40-percent; walmart.id=09fa06f1-d48f-4331-b304-962351628d00; _ga=GA1.2.621116102.1604796208; _gid=GA1.2.277603389.1604796208; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; _pxvid=6a906779-215b-11eb-8b2e-0242ac120002; DYN_USER_ID=67580559-be36-433f-a489-d98e44ea4b96; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4lE3R78tOCzf5oqjeoCyS3H05m3hzgaXwN1STznaWKE+/mQ3ile+7ssKnyiqLFfns+k1ywS8xE58mi/5ybksWpR+KS5BlQpMa1nos97k2sq7bYQCy774TUE5mrXNmprrzj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0lJlHL978H9Z5PKnKHwe8GPtPC56OL433Dk+vTttmq2eHdBtPrB6vbl/Zh6XkbcFHb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEHIMdpRi0iatb7S4HHlAgSoDZHQljs/cWHM0t1Ac18CxDtPMgO/gEqQaSRxkCKFtv7TF0cSrJ9/5larmnocIcWafIZ3T1gAXYw2ULyTQuSCQP44VNKds/cuTqqP7xb674A==; LT=1604796207945; _fbp=fb.1.1604796207799.1827601776; s_visit=1; s_cc=true; _gcl_au=1.1.376722026.1604796208; __gads=ID=fb9b8a7b64e01c7e:T=1604796208:S=ALNI_MZYXcI7TCkbwPa0hlOS7alB-q3gcQ; NEXT_GEN.ENABLED=1; cartId=7a7a62de-7ca9-4517-b2f5-b2c2344c2c5f; akavpau_CA_PROD_Product_page=1604798188~id=d4e4f11761809a1dceae03fc37f3f4db; s_vi=[CS]v1|2FD3A2E18515D50F-60000A1C248869D7[CE]; s_ecid=MCMID%7C35491274262018340851842861422459610209; AMCV_C4C6370453309C960A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18575%7CMCMID%7C35491274262018340851842861422459610209%7CMCAAMLH-1605402690%7C7%7CMCAAMB-1605402690%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1604805090s%7CNONE%7CMCSYNCSOP%7C411-18582%7CvVersion%7C5.0.1%7CMCAID%7C2FD3A2E18515D50F-60000A1C248869D7; og_session_id=af0a84f8847311e3b233bc764e1107f2.360940.1604797891; og_session_id_conf=af0a84f8847311e3b233bc764e1107f2.360940.1604797891; _scid=933cd410-94a7-4353-a98e-86d1063a6345; _pin_unauth=dWlkPU5USmlaR0ZqWVdNdE9URXdNQzAwTnpCaUxUazRZbU10TlRVME1UUXdPRFF3TW1OaA; _sctr=1|1604725200000; wm.device_fingerprint=4cb9e910-5416-4597-9ba3-952781196074; ENV=ak-cdc-prod; bstc=biSsveIl1l-1GSswbUbQSU; xpa=2lwWQ|2oqzF|63K3S|6V3fl|6iOkF|6rNcs|7Xi3l|DwTRU|GpBCe|HbOxV|IJ4rZ|Jeavw|KpQ33|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Pic8m|Q0IHr|SIe2y|SNvE3|VIGCY|X92ox|XBdGQ|YJsua|YcwI-|YxLOx|_vY-K|a4vv4|biw7H|c8ThE|fJumS|hcz5Y|jeBOs|kZ1Eq|lZnE7|mOlOu|o5Sri|pldE2|rwaVg|sGGbM|wx8xe|yI7_k; exp-ck=2oqzF26V3flk6iOkF46rNcs27Xi3l1DwTRU1GpBCe1HbOxV1IJ4rZ1Jeavw1KpQ334MZ9tt1Oqgc14Pic8m1SIe2y1SNvE31X92ox4XBdGQ1YJsua5YcwI-1YxLOx1a4vv41c8ThE1fJumS3kZ1Eq1lZnE76o5SribpldE21rwaVg4sGGbM4wx8xe1yI7_k1; TS01f4281b=01c5a4e2f9b55e106b220e4fe2709b3f172f5689a58be00ff566a1b61436e4bc553f8cbbef4a708b6e4ca3519fb337691a71a38cd9; TS011fb5f6=01c5a4e2f9b55e106b220e4fe2709b3f172f5689a58be00ff566a1b61436e4bc553f8cbbef4a708b6e4ca3519fb337691a71a38cd9; TS0175e29f=01c5a4e2f9b55e106b220e4fe2709b3f172f5689a58be00ff566a1b61436e4bc553f8cbbef4a708b6e4ca3519fb337691a71a38cd9; xpm=1%2B1604799816%2BSSsOobpNazV42hodX3uuDg~%2B0; s_gnr=1604799816315-Repeat; WM.USER_STATE=GUEST|Guest; _px3=42b3911639ebf9a0f2f6567afed9c6838ec6310c414a8f9ea397ea8f7a6f3eee:60q9PLhpBtvxP2SeEfXf1SlZuiPYbggvkBsuSkc8u7LFUU+Pb3Dotkm4qJpICJ03Qf28tx4PJa3K8apT9gZWMw==:1000:g5NkjM+ps184IhNwfaTwcTyb9EshGG81Wh8P1FR+O8CuJpnCPjK+7oS1DAgok/fAubMWc83q5U9to+USZONyHRgSUYRA87uiPmK84iV7djQZKswWB6iqJWyzZvshoJp8KqpvDzBpWxyGKCsZL0VT6KokBOkEwyWbnIAW4dyAwh0=; _uetsid=562e33a0215f11ebacc0ffcc90f15867; _uetvid=562e76f0215f11ebb7b6af05bfd36bba; _pxde=6500bcb5cbdfe2220f8932aa20da0bc6fc3244b96bef0c0470c52fb1d12fe6c3:eyJ0aW1lc3RhbXAiOjE2MDQ3OTk4NTQyNTgsImZfa2IiOjAsImlwY19pZCI6W119; walmart.nearestPostalCode=H3C9Z0; walmart.nearestLatLng="45.4978,-73.5485"; authDuration={"lat":"1604799875925000","lt":"1604799875925000"}; seqnum=10; akavpau_CA_PROD_Entire_Site=1604800176~id=7463b9144a8923dde4c0710cefb31e6e; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DCheckout%2526link%253DNext%2526region%253DshippingAddressForm%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DCheckout%2526pidt%253D1%2526oid%253DNext%2526oidt%253D3%2526ot%253DSUBMIT',
            #'wm_qos.correlation_id': '4a005237-026-175a54ed043916,4a005237-026-175a54ed043fdb,4a005237-026-175a54ed043fdb'
        }
        #links
        link = 'https://www.walmart.ca/api/checkout-page/checkout/email?availStore=3165&postalCode=H3G0E1'
        shipping_link = 'https://www.walmart.ca/api/checkout-page/checkout/address?lang=en&availStore=3165&slotBooked=false'
        postal_link = 'https://www.walmart.ca/api/checkout-page/edd?postalCode=H3G0E1'
        summary_link ='https://www.walmart.ca/api/checkout-page/payments/summaryhttps://www.walmart.ca/api/checkout-page/payments/summary'
        ###########################################################
        email_data = '{"emailAddress":"lzweijinwei@yahoo.ca"}'
        shipping_data = '{"fulfillmentType":"SHIPTOHOME","deliveryInfo":{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G0E1","phone":"4387258504","saveToProfile":true,"country":"CA","locationId":null,"overrideAddressVerification":false}}'
        postal_data = '{"order":{"subTotal":147,"fulfillmentType":"SHIPTOHOME","isPOBoxAddress":false},"sellers":[{"sellerId":"0","itemTotal":147,"items":[{"skuId":"6000197280859","offerId":"6000197280859","quantity":1,"shipping":{"options":["STANDARD"],"type":"PARCEL","isShipAlone":false},"isDigitalItem":false,"isFreightItem":false}]}]}'
        #data = {"fulfillmentType":"SHIPTOHOME","deliveryInfo":{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G 0E1","phone":"4387258504","saveToProfile":'true',"country":"CA","locationId":'null',"overrideAddressVerification":'false'}}
        summary_data = '{"orderTotal":169.01,"paymentMethods":[{"piHash":{"pan":"4520027175666631","cvv":"032","encryption":{"integrityCheck":"a8d2040d4052860d","phase":"0","keyId":"4e5c56c2"}},"cardType":"CREDIT_CARD","pmId":"VISA","cardLast4Digits":"6631","referenceId":"1w8nq"}]}'
        r_email= self.session.post(link, headers=header, json=email_data)
        r_shipping = self.session.post(shipping_link, headers=header, json=shipping_data)
        r_postal = self.session.post(postal_link, headers=header, json=postal_data)
        r_summary = self.session.post(summary_link, headers=header, json=summary_data)
        print(r_summary.text)

walmart = Walmart()