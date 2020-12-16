from selenium_wrapper.bot import *
from selenium_wrapper import bot
from time import sleep
import platform
from persons.yi import Yi
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class UnavailableException(Exception):
    pass

bot.AUTO_QUIT=False

class LV(Bot):

    def __init__(self, driver_path, person, headless=False):
        super(LV, self).__init__(driver_path, headless=headless)
        self.person=person


    def atc(self, product_url):
        v_atc = Verification(type='xpath', text='//*[@class="lv-product-purchase-button lv-button -primary lv-product-purchase__button -fullwidth"]')
        v_view_cart = Verification(type='xpath', text='//*[contains(text(), "View my cart")]')
        v_proceed = Verification(type='xpath', text='//*[@class="goToCheckout proceedBtn tagClick"]')
        v_continue_guest = Verification(type='xpath', text='//*[@id="continueWithoutLogging"]')
        v_FirstName = Verification(type='xpath', text='//*[@id="firstName"]')

        self.visit_site(product_url, v_atc)
        atc_btn = self.find(verification=v_atc)
        if atc_btn.text == 'Call for Availability':
            print(f"WARNING: {product_url} atc button appears to say Call for Availability")
            raise UnavailableException

        self.action(atc_btn.click, verification=v_view_cart, action_name='placing to cart')
        view_vart_btn = self.find(verification=v_view_cart)
        self.action(view_vart_btn.click, verification=v_proceed, action_name='view bag')
        proceed_btn = self.find(verification=v_proceed)
        self.action(proceed_btn.click, verification=v_continue_guest, action_name='proceed')
        continue_guest_btn = self.find(verification=v_continue_guest)
        self.action(continue_guest_btn.click, verification=v_FirstName, action_name='continue as guest')

    def enter_billing_info(self):
        v_FirstName = Verification(type='xpath', text='//*[@id="firstName"]')
        v_LastName = Verification(type='xpath', text='//*[@id="lastName"]')
        v_address = Verification(type='xpath', text='//*[@id="address1"]')
        v_postalcode = Verification(type='xpath', text='//*[@id="postalCode"]')
        v_city = Verification(type='xpath', text='//*[@id="city"]')
        v_phone = Verification(type='xpath', text='//*[@id="phoneNumber"]')
        v_state = Verification(type='xpath', text='//*[@id="state"]')

        me = self.person
        fields = {v_FirstName:me.firstName,
                  v_LastName:me.lastName,
                  v_address:me.address,
                  v_postalcode:me.postal_code,
                  v_city:me.city,
                  v_phone:me.phone,
                  #v_email:me.email
                  }

        for verification, value in fields.items():
            input_box = self.find(verification=verification)
            self.action(input_box.send_keys, value, input_box_verification=True)

        state_select = self.find(verification=v_state)
        select=Select(state_select)
        #using BC here because in html value=BC,
        self.action(select.select_by_value, me.province)

    def submit_shipping(self):
        pick_up_btn=None
        try:
            v_pickup = Verification(type='xpath', text='//*[@id="clickAndCollect"]')
            pick_up_btn = self.find(verification=v_pickup)
        except:
            print('collect in store not available, doing delivery instead')
        if pick_up_btn is None:
            self.enter_billing_info()
        else:
            self.choose_pickup_location(pick_up_btn)

        v_email = Verification(type='xpath', text='//*[@id="email"]')
        email_input = self.find(verification=v_email)
        self.action(email_input.send_keys, self.person.email, input_box_verification=True)


    def choose_pickup_location(self, pick_up_btn):
        v_holt_renfrew = Verification(type='xpath', text='//*[@id="UVC"]')

        try:
            self.action(pick_up_btn.click, verification=v_holt_renfrew)
        except:
            self.press_key(Keys.ESCAPE, verification=v_holt_renfrew)

        holt_renfrew_radio = self.find(verification=v_holt_renfrew)
        self.action(holt_renfrew_radio.click)


if __name__=='__main__':
    me = Yi('csv')
    lv = LV('../chromedriver.exe',me, headless=False)

    #lv.atc('https://ca.louisvuitton.com/eng-ca/products/my-everything-duo-xs-monogram-shawl-nvprod2540101v')
    lv.atc('https://ca.louisvuitton.com/eng-ca/products/spring-street-monogram-vernis-nvprod1280190v')
    lv.submit_shipping()

    #taskkill /im chromedriver.exe /f
