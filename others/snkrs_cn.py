from shopifyWebhook import notifyDisc_snkrs_cn, notifyDisc_snkrs_non_product_cn,notifyDisc_nike_cn
from collections import OrderedDict
import time
import json
import random
import requests
import concurrent.futures
from random import randint
from sites.module_class.Nike import Nike
from shopifyMonitor import findDiff

def call_discord(base_url, data):
    #only for products obj
    if "productInfo" in data:
        #product info retrieve the merch info first
        info = data["productInfo"][0]
        product = info["merchProduct"]
        product_sale = info["merchPrice"]
        product_content = info["productContent"]

        #assign params to corresponding var
        image_url = info["imageUrls"]["productImageUrl"]
        slug = product_content["slug"]
        title = product_content["title"]
        link = base_url + slug
        active = product["status"]
        style_code = product["styleCode"]
        exclusiveAccess = product["exclusiveAccess"]
        price = product_sale["currentPrice"]
        #availiability, launch date and format
        availability = info["availability"]["available"]

        #some product dont have the attribute of launchview
        if "launchView" in info:
                launch = info["launchView"]
                method = launch["method"]
                date = launch["startEntryDate"]
                notifyDisc_snkrs_cn(image_url, link, title, price, active, style_code, exclusiveAccess, availability, method,
                                 date)
        else:
            notifyDisc_snkrs_cn(image_url, link, title, price, active, style_code, exclusiveAccess, availability)
    else:
        info = data["publishedContent"]["properties"]
        seo = info["seo"]
        date = data["publishedContent"]["viewStartDate"]
        description = seo["description"]
        title = seo["title"]
        link = base_url + seo["slug"]
        image_url = info["coverCard"]["properties"]["squarishURL"]
        #execute the discord notification
        notifyDisc_snkrs_non_product_cn(image_url, link, title, date, description)

def call_discord_nike(base_url, data):
    info = data["publishedContent"]["properties"]
    title = info["title"]
    link = base_url + info["seo"]["slug"]
    image_url = info["productCard"]["properties"]["squarishURL"]
    #other detailed info
    info_product = data["productInfo"][0]
    price = info_product["merchPrice"]["currentPrice"]
    styleColor = info_product["merchProduct"]["styleColor"]
    status = info_product["merchProduct"]["status"]
    date = info_product["merchProduct"]["commerceStartDate"]
    availability = info_product["availability"]["available"]

    notifyDisc_nike_cn(image_url,link, title, price, status, styleColor, availability, date)

def loadProxy():
    with open("proxy.json") as proxy_list:
        proxy = json.load(proxy_list)
        # print(proxy)
        proxiesid = {'http': "http://" + random.choice(proxy)}
    return proxiesid

def nike_web(the_url):
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem

    url = the_url
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return url, user_agent_rotator


def monitor_snkrs(base_url, api_url):
        while True:
            #keep getting different user_agent each iteration
            url, user_agent_rotator = nike_web(api_url)
            try:
                proxy = loadProxy()
                headers = {
                    'upgrade-insecure-requests' : '1',
                    'cache-control' : 'no-cache',
                    'Pragma' : 'no-cache',
                    'user-agent' : user_agent_rotator.get_random_user_agent(),
                    'sec-fetch-mode' : 'navigate',
                    'sec-fetch-user' : '?1',
                    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'sec-fetch-site' : 'none',
                    'accept-encoding' : 'gzip, deflate, br',
                    'accept-language' : 'en-US,en;q=0.9'
                }
                requests.headers = OrderedDict(headers)
                r = requests.get(url= url, proxies = proxy).text
                #retrive the objects from the json list
                current_status = json.loads(r)["objects"]
                nike = Nike(current_status, 'snkrs_cn')
                diff = findDiff(nike.current_status_ana(), json.loads((nike.query_db()).status))


                #notify discord for all the items
                if len(diff) != 0:
                        for item in current_status:
                            try:
                                if item["id"] in diff:
                                    call_discord(base_url, item)
                            except Exception as e:
                                print(e)
                                pass

                #now database should be updated
                nike.update_db(nike.query_db(), nike.current_status_ana())

                #time.sleep(randint(50,60))
                time.sleep(randint(10, 20))
            except Exception as e:
                time.sleep(randint(30, 60))
                print("error is ")
                print(e)


def monitor_nike(base_url, api_url):
    while True:
        # keep getting different user_agent each iteration
        url, user_agent_rotator = nike_web(api_url)
        try:
            proxy = loadProxy()
            headers = {
                'upgrade-insecure-requests': '1',
                'cache-control': 'no-cache',
                'Pragma': 'no-cache',
                'user-agent': user_agent_rotator.get_random_user_agent(),
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'sec-fetch-site': 'none',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
            requests.headers = OrderedDict(headers)
            r = requests.get(url=url, proxies=proxy).text
            # retrive the objects from the json list
            # current_status = json.loads(r)["objects"]
            current_status = json.loads(r)["data"]["filteredProductsWithContext"]["objects"]
            #create the nike object
            nike = Nike(current_status, 'nike_cn')
            #get the status from db, and retrieve the id from the current status that retrived from api
            old_status_db = json.loads((nike.query_db()).status)
            current_status_id_list = nike.current_status_ana()
            diff = findDiff(current_status_id_list, old_status_db)
            current_status_id_available_list = nike.current_status_with_availability()

            # notify discord for all the items
            if len(diff) != 0:
                #only create this list when there is diff
                for item in current_status:
                    try:
                        if item["id"] in diff:
                            call_discord_nike(base_url, item)
                    except Exception as e:
                        print(e)
                        pass
                for item in diff:
                    old_status_db[item] = (current_status_id_available_list[item])

                # now database should be updated
                nike.update_db(nike.query_db(), old_status_db)

            # check if restocks
            check_avail(current_status_id_available_list, old_status_db, base_url, current_status, nike)

            # time.sleep(randint(50,60))
            time.sleep(randint(10,20))

        except Exception as e:
            time.sleep(randint(30,60))
            print("error is ")
            #print(e)

def check_avail(current, old, base_url, current_data, nike):
    for key, value in old.items():
        if value == False or value == "N/A":
            if current[key] == True:
                data = next((item for item in current_data if item['id'] == key), None)
                call_discord_nike(base_url, data)
                old[key] = current[key]
                nike.update_db(nike.query_db(), old)


if(__name__ == "__main__"):
    api_snkr_cn = "https://api.nike.com/product_feed/threads/v2/?anchor=0&count=21&filter=marketplace%28CN%29&filter=language%28zh-Hans%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29"
    api_nike_cn = "https://api.nike.com/cic/browse/v1?queryid=filteredProductsWithContext&anonymousId=V7KpaHChtIdYMZ4P4eDSi&uuids=0f64ecc7-d624-4e91-b171-b83a03dd8550,16633190-45e5-4830-a068-232ac7aea82c&language=zh-Hans&country=CN&channel=NIKE&sortBy=newest"
    nike_ca_base_url = "https://www.nike.com/cn/u/"
    snkrs_ca_base_url = "https://www.nike.com/cn/launch/t/"
    try:
        with concurrent.futures.ThreadPoolExecutor() as player:
            for num in range(1, 10):
                if num % 2 == 0:
                    player.submit(monitor_nike,nike_ca_base_url, api_nike_cn)
                else:
                    player.submit(monitor_snkrs,snkrs_ca_base_url,api_snkr_cn)
                time.sleep(2)
    except Exception as e:
        # print(e)
        pass

    #monitor_nike(nike_ca_base_url, api_nike_ca)