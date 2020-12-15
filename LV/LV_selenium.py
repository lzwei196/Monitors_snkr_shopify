from selenium_wrapper.bot import *
from selenium_wrapper import bot
from time import sleep
import platform
from persons.yi import Yi

class UnavailableException(Exception):
    pass

bot.AUTO_QUIT=False

class LV(Bot):

    def __init__(self, driver_path, headless=False):
        super(LV, self).__init__(driver_path, headless=headless)


    def atc(self, product_url):
        v_atc = Verification(type='xpath', text='//*[@class="lv-product-purchase-button lv-button -primary lv-product-purchase__button -fullwidth"]')
        v_view_cart = Verification(type='xpath', text='//*[contains(text(), "View my cart")]')
        v_proceed = Verification(type='xpath', text='//*[@class="goToCheckout proceedBtn tagClick"]')
        v_continue_guest = Verification(type='xpath', text='//*[@id="continueWithoutLogging"]')
        v_FirstName = Verification(type='xpath', text='//*[@id="firstName"]')

        self.visit_site(product_url, v_atc)
        atc_btn, _ = self.find(verification=v_atc)
        if atc_btn.text == 'Call for Availability':
            print(f"WARNING: {product_url} atc button appears to say Call for Availability")
            raise UnavailableException

        self.action(atc_btn.click, verification=v_view_cart, action_name='placing to cart')
        view_vart_btn, _ = self.find(verification=v_view_cart)
        self.action(view_vart_btn.click, verification=v_proceed, action_name='view bag')
        proceed_btn, _ = self.find(verification=v_proceed)
        self.action(proceed_btn.click, verification=v_continue_guest, action_name='proceed')
        continue_guest_btn, _ = self.find(verification=v_continue_guest)
        self.action(continue_guest_btn.click, verification=v_FirstName, action_name='continue as guest')

    def enter_deliver_info(self, csv):
        v_FirstName = Verification(type='xpath', text='//*[@id="firstName"]')
        v_LastName = Verification(type='xpath', text='//*[@id="firstName"]')
        v_address = Verification(type='xpath', text='//*[@id="firstName"]')
        v_postalcode = Verification(type='xpath', text='//*[@id="firstName"]')
        v_city = Verification(type='xpath', text='//*[@id="firstName"]')
        v_state = Verification(type='xpath', text='//*[@id="firstName"]')
        v_phone = Verification(type='xpath', text='//*[@id="firstName"]')
        v_email = Verification(type='xpath', text='//*[@id="firstName"]')
        me = Yi(csv)
        fields = {v_FirstName:me.firstName,
                  v_LastName:me.lastName,
                  v_address:me.address,
                  v_postalcode:me.postal_code,
                  v_city:me.city,
                  v_state:me.province,
                  v_phone:me.phone,
                  v_email:me.email}

        for verification, value in fields.items():
            input_box, _ = self.find(verification=verification)
            self.action(input_box.send_keys, value, input_box_verification=True)




if __name__=='__main__':
    lv = LV('../chromedriver.exe', headless=False)

    lv.atc('https://ca.louisvuitton.com/eng-ca/products/my-everything-duo-xs-monogram-shawl-nvprod2540101v')
    lv.enter_deliver_info('123')
