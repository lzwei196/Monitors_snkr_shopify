from selenium_wrapper.bot import Verification

v_credit_card_num = Verification(type='xpath', text='//*[@id="creditCardNumber"]')
v_proceed = Verification(type='xpath', text='//*[@id="globalSubmit"]')
v_FirstName = Verification(type='xpath', text='//*[@id="firstName"]')
v_acc = Verification(type='xpath', text='//*[@id="loginloginForm"]')
v_acc_pwd = Verification(type='xpath', text='//*[@id="passwordloginForm"]')
v_sign_in = Verification(type='xpath', text='//*[@id="loginSubmit_"]')
v_credit_card_holder = Verification(type='xpath', text='//*[@id="creditCardHoldersName"]')
v_credit_card_month = Verification(type='xpath', text='//*[@id="expirationMonth"]')
v_credit_card_year = Verification(type='xpath', text='//*[@id="expirationYear"]')
v_credit_card_csv = Verification(type='xpath', text='//*[@id="cardVerificationNumber_0"]')
v_LastName = Verification(type='xpath', text='//*[@id="lastName"]')
v_address = Verification(type='xpath', text='//*[@id="address1"]')
v_postalcode = Verification(type='xpath', text='//*[@id="postalCode"]')
v_city = Verification(type='xpath', text='//*[@id="city"]')
v_phone = Verification(type='xpath', text='//*[@id="phoneNumber"]')
v_state = Verification(type='xpath', text='//*[@id="state"]')
v_atc = Verification(type='xpath',
                     text='//*[@class="lv-product-purchase-button lv-button -primary lv-product-purchase__button -fullwidth"]')
v_view_cart = Verification(type='xpath', text='//*[contains(text(), "View my cart")]')
v_proceed_1 = Verification(type='xpath', text='//*[@id="proceedToCheckoutButtonTop"]')
v_cfa = Verification(type='xpath',
                     text='//*[@class=""lv-product-purchase-button lv-button -primary lv-product-purchase__button -fullwidth -no-pointer""]')
v_out_of_stock = Verification(type='xpath', text='//*[@id="lv-product-add-to-cart__error"]')
v_agree_to_terms = Verification(type='xpath', text='//*[@data-evt-content-id="terms_of_sales"]')
v_submit_order = Verification(type='xpath', text='//*[@id="globalSubmitTop"]')
v_delivery = Verification(type='xpath', text='//*[@id="standardShipping"]')
v_select_address = Verification(type='xpath', text='//*[@id="selectAnAddress"]')
v_status_500=Verification(type='xpath', text='//*[@class="lv-product-add-to-cart__error"]')
v_notify_me=Verification(type='xpath', text='//*[@class="lv-product-purchase-button lv-button -primary lv-product-purchase__button -fullwidth t011-enable-pointer"]')
v_call_for_ava=Verification(type='xpath', text='//*[@class="lv-product-purchase-button lv-button -primary -no-pointer"]')


# <p class="lv-product-add-to-cart__error">Request failed with status code 500</p>
