from selenium_wrapper.bot import *
import requests
from time import sleep

AUTO_QUIT=True

class Bestbuy(Bot):
    def __init__(self, driver_path, headless=False):
        super(Bestbuy, self).__init__(driver_path, headless=headless)

    def login(self, urls=None):
        if urls is None:
            urls=['https://www.bestbuy.ca/en-ca', 'https://www.bestbuy.ca/en-ca/basket']
        #just to get some cookies
        for site in urls:
            self.visit_site(site)

        cookies_to_set=['rxVisitor', 'gbi_sessionId']
        cookies_to_set = set(cookies_to_set)

        for i in range(10):
            sleep(0)
            cookies = self.browser.get_cookies()
            for cookie in cookies:
                if cookie['name'] in cookies_to_set:
                    cookies_to_set.remove(cookie['name'])
            if len(cookies_to_set) < 1:
                return



class Walmart(Bot):
    def __init__(self, driver_path, headless=False):
        super(Walmart, self).__init__(driver_path, headless=headless)

    def login(self, urls=None):
        if urls is None:
            urls=['https://www.walmart.ca']
        #just to get some cookies
        for site in urls:
            self.visit_site(site)
        print('sleeping 10 second to wait for all cookies to load')
        sleep(10)




if __name__ == "__main__":
    crawler=Bestbuy('../chromedriver.exe', headless=True)
    crawler.login()
    cookies = crawler.browser.get_cookies()

    session = requests.session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
        print(cookie['name'], cookie['value'])


