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
    v_credit_card_num = Verification(type='xpath', text='//*[@id="creditCardNumber"]')
    v_proceed = Verification(type='xpath', text='//*[@id="globalSubmit"]')
    v_FirstName = Verification(type='xpath', text='//*[@id="firstName"]')


    def __init__(self, driver_path, person, headless=False):
        super(LV, self).__init__(driver_path, headless=headless)
        self.person=person


    def log_in(self):
        v_acc = Verification(type='xpath', text='//*[@id="loginloginForm"]')
        v_acc_pwd = Verification(type='xpath', text='//*[@id="passwordloginForm"]')
        v_sign_in = Verification(type='xpath', text='//*[@id="loginSubmit_"]')
        v_proceed = self.v_proceed
        v_credit_card_num = self.v_credit_card_num

        acc_input = self.find(verification=v_acc)
        self.action(acc_input.send_keys, self.person.get_LV_acc().username, input_box_verification=True)
        acc_pwd_input = self.find(verification=v_acc_pwd)
        self.action(acc_pwd_input.send_keys, self.person.get_LV_acc().pwd, input_box_verification=True)
        acc_sign_in = self.find(verification=v_sign_in)
        self.action(acc_sign_in.click, verification=v_proceed, action_name='proceed to billing')



    def fill_credit_card(self):
        v_credit_card_num = self.v_credit_card_num
        v_credit_card_holder = Verification(type='xpath', text='//*[@id="creditCardHoldersName"]')
        v_credit_card_month = Verification(type='xpath', text='//*[@id="expirationMonth"]')
        v_credit_card_year = Verification(type='xpath', text='//*[@id="expirationYear"]')
        v_credit_card_csv = Verification(type='xpath', text='//*[@id="cardVerificationNumber_0"]')

        card_num_input = self.find(verification=v_credit_card_num)
        self.action(card_num_input.send_keys, self.person.card_num, input_box_verification=True)
        card_holder_input = self.find(verification=v_credit_card_holder)
        self.action(card_holder_input.send_keys, f'{self.person.firstName} {self.person.lastName}' , input_box_verification=True)
        card_csv_input = self.find(verification=v_credit_card_csv)
        self.action(card_csv_input.send_keys, self.person.csv, input_box_verification=True)

        card_month = self.find(verification=v_credit_card_month)
        select=Select(card_month)
        self.action(select.select_by_value, str(int(me.card_month))) #to format 01 to 1

        card_year = self.find(verification=v_credit_card_year)
        select=Select(card_year)
        self.action(select.select_by_value, me.card_year)

    def choose_pickup_location(self, pick_up_btn):
        v_holt_renfrew = Verification(type='xpath', text='//*[@id="UVC"]')

        try:
            self.action(pick_up_btn.click, verification=v_holt_renfrew)
        except:
            self.press_key(Keys.ESCAPE, verification=v_holt_renfrew)

        holt_renfrew_radio = self.find(verification=v_holt_renfrew)
        self.action(holt_renfrew_radio.click)

    def enter_billing_info(self):
        v_FirstName = self.v_FirstName
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

    def atc(self, product_url):
        v_atc = Verification(type='xpath', text='//*[@class="lv-product-purchase-button lv-button -primary lv-product-purchase__button -fullwidth"]')
        v_view_cart = Verification(type='xpath', text='//*[contains(text(), "View my cart")]')
        v_proceed_1 = Verification(type='xpath', text='//*[@id="proceedToCheckoutButtonTop"]')
        v_continue_guest = Verification(type='xpath', text='//*[@id="continueWithoutLogging"]')
        v_FirstName = self.v_FirstName

        self.visit_site(product_url, v_atc)
        atc_btn = self.find(verification=v_atc)
        if atc_btn.text == 'Call for Availability':
            print(f"WARNING: {product_url} atc button appears to say Call for Availability")
            raise UnavailableException

        self.action(atc_btn.click, verification=v_view_cart, action_name='placing to cart')
        view_vart_btn = self.find(verification=v_view_cart)
        self.action(view_vart_btn.click, verification=v_proceed_1, action_name='view bag')
        proceed_btn = self.find(verification=v_proceed_1)

        #todo catch this by
        self.action(proceed_btn.click, verification=v_continue_guest, action_name='proceed')
        self.log_in()

    def purchase(self):
        pick_up_btn=None

        #do pick up, or delivery when pick up is not available
        try:
            v_pickup = Verification(type='xpath', text='//*[@id="clickAndCollect"]')
            pick_up_btn = self.find(verification=v_pickup)
        except:
            print('collect in store not available, doing delivery instead')

        if pick_up_btn is None:
            pass
            # print('no pickup')
            # exit(0)
            # self.enter_billing_info()
        else:
            sleep(5)
            print('slight wait before collecting in store')
            self.choose_pickup_location(pick_up_btn)
            pick_up_btn=True

        #rest of the workflow
        v_proceed = self.v_proceed
        v_credit_card_num = self.v_credit_card_num
        v_agree_to_terms = Verification(type='xpath', text='//*[@data-evt-content-id="terms_of_sales"]')
        v_submit_order = Verification(type='xpath', text='//*[@id="globalSubmitTop"]')

        # self.browser.execute_script(
        #     "fireEvent('proceedToBilling');startChain()")
        # self.browser.execute_script(
        #     "fireEvent('proceedToBilling');startChain()")
        # self.browser.execute_script(
        #     "fireEvent('proceedToBilling');startChain()")
        proceed_btn = self.find(verification=v_proceed)
        self.action(proceed_btn.click, verification=v_credit_card_num, action_name='proceed to billing')
        self.fill_credit_card()

        proceed_btn = self.find(verification=v_proceed) #same id but should be on different page by now
        self.action(proceed_btn.click, verification=v_agree_to_terms, action_name='proceed to checkout')

        #submit_order
        agree_terms_btn = self.find(verification=v_agree_to_terms)
        self.action(agree_terms_btn.click, verification=v_submit_order, action_name='clicking agree to terms')
        submit_order_btn = self.find(verification=v_submit_order)
        self.action(submit_order_btn.click,  action_name='clicking SUBMIT ORDER')


        #todo check if pick_up_btn is not None, if its not None need to call self.enter_billing_info()



if __name__=='__main__':
    me = Yi('343')
    lv = LV('../chromedriver.exe',me, headless=True)

    #lv.atc('https://ca.louisvuitton.com/eng-ca/products/my-everything-duo-xs-monogram-shawl-nvprod2540101v')
    lv.atc('https://ca.louisvuitton.com/eng-ca/products/spring-street-monogram-vernis-nvprod1280190v')
    #lv.atc('https://ca.louisvuitton.com/eng-ca/products/mini-pochette-accessoires-monogram-001025')
    lv.purchase()

    #taskkill /im chromedriver.exe /f
