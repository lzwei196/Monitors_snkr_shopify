from selenium_wrapper.bot import *
import requests

class Bestbuy(Bot):
    def __init__(self, driver_path, headless=False):
        super(Bestbuy, self).__init__(driver_path, headless=headless)

    def login(self):
        #just to get some cookies
        self.visit_site('https://www.bestbuy.ca/en-ca')
        self.visit_site('https://www.bestbuy.ca/en-ca/basket')




if __name__ == "__main__":
    crawler=Bestbuy('../chromedriver.exe', headless=False)
    crawler.login()
    cookies = crawler.browser.get_cookies()

    session = requests.session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
        print(cookie['name'], cookie['value'])
    session.get('https://www.bestbuy.ca/en-ca')

