from selenium_wrapper.bot import *
from time import sleep
import platform

class UnavailableException(Exception):
    pass

class LV(Bot):
    def __init__(self, driver_path, headless=False):
        super(LV, self).__init__(driver_path, headless=headless)

    def atc(self, product_url):
        # v_home_page = Verification(type='xpath', text='//*[@class="lv-header-service-shipping__label"]')
        # self.visit_site('https://ca.louisvuitton.com/eng-ca/homepage', verification=v_home_page)
        # sleep(5)

        v_atc =Verification(type='xpath', text='//*[contains(text(), "Place in Cart")]')
        v_view_cart = Verification(type='xpath', text='//*[@class ="lv-smart-link lv-button -primary"]')
        v_proceed = Verification(type='xpath', text='//*[@class ="goToCheckout proceedBtn tagClick"]')


        self.visit_site(product_url, v_atc)
        atc_btn, _ = self.find(verification=v_atc)
        if atc_btn.text == 'Call for Availability':
            print(f"WARNING: {product_url} atc button appears to say Call for Availability")
            raise UnavailableException
        else:
            self.action(atc_btn.click, verification=v_view_cart, action_name='placing to cart')
            view_vart_btn, _ = self.find(verification=v_view_cart)
            self.action(view_vart_btn.click, verification=v_proceed, action_name='view  cart')
            proceed_btn, _ = self.find(verification=v_proceed)
            self.action(proceed_btn.click, verification=None, action_name='proceed')



if __name__=='__main__':
    lv = LV('../chromedriver.exe', headless=False)
    lv.atc('https://ca.louisvuitton.com/eng-ca/products/my-everything-duo-xs-monogram-shawl-nvprod2540101v')