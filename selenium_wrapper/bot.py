from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from collections import namedtuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import traceback
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from util.decorators import *

# import this variable when using the class Snkr
Verification = namedtuple('Verification', 'type text')
INTERNAL_LOGGING = None
VERBOSE = True
AUTO_QUIT = True

@debug
def prints(*args):
    # overloading default print for this file so that you can turn off all prints with VERBOSE
    # use this prints instead of print() for this file
    global INTERNAL_LOGGING
    if VERBOSE:
        print(*args)
    if INTERNAL_LOGGING:
        INTERNAL_LOGGING.debug(*args)

class Bot:

    def __init__(self, driver_path, headless=False):
        # set the brower object and find function types
        options = Options()
        options.headless = headless
        self.browser = webdriver.Chrome(driver_path, chrome_options=options)
        self.driver_path = driver_path
        # store functions in dictionaries so we can make our own find functions with error handling and logs
        # todo, incompleted list of functions
        self.types={'class': self.browser.find_element_by_class_name,
                   'xpath': self.browser.find_element_by_xpath,
                    'id': self.browser.find_element_by_id}
        #simmilar idea as above
        # todo, incompleted list of By types
        self.verification_types={'xpath': By.XPATH}
        prints('finished init with', driver_path)

    def __del__(self):
        if AUTO_QUIT is True:
            self.browser.close()
            sleep(3)
            self.browser.quit()

    def scroll_to_element(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def enable_network_logs(self):
        # recreate browser object with performance logging
        self.browser.close()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        self.browser = webdriver.Chrome(self.driver_path, options=chrome_options)

    def get_performance_logs(self):
        logs = self.browser.get_log('performance')
        return logs

    def set_logger(self,logfile):
        # logfile: string
        # set log file
        global INTERNAL_LOGGING
        self.logfile = logfile
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        fh = logging.FileHandler(self.logfile)
        self.log.addHandler(fh)
        INTERNAL_LOGGING = self.log
        with open(self.logfile, 'w') as fout:
            fout.write('\n')

    def visit_site(self, url, verification=None):
        # visit url, check for verification elements, if element does not show up method returns False,
        # state of self.browser is changed after functions runs
        # return: Boolean
        self.browser.get(url)
        if verification:
            success = self.verify(verification)
            if success:
                prints('successfully loaded page %s' % url)
                return True
            else:
                prints('failed to load page %s' % url)
                return False

    def remove_element(self,element):
        self.browser.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

    def verify(self,verification):
        # wait up to 3 seconds for an element to show up
        # return: Boolean
        veri_type = verification.type
        text = verification.text
        method = self.verification_types[veri_type]
        delay = 10  # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.element_to_be_clickable((method, text)))
            return True
        except TimeoutException:
            prints('timed out waiting for element %s to show up' % text)
            return False
        except Exception as e:
            traceback.print_exc()
            return False

    def generate_action_name(self, element, act):
        name = element.get_attribute('name')
        id = element.get_attribute('id')
        class_ = element.get_attribute('class')
        arr = [name, id, class_]
        for item in arr:
            if item is not None and item != '':
                return '%s on %s' % (act, item)
        return '%s on %s' % (act, 'unknown element')

    def action(self, action, *args, verification=None, input_box_verification = None, action_name=None, retries = 0):
        #if input_box_verification is passed auto check if text is entered
        element = action.__self__
        if retries >3:
            traceback.print_exc()
            raise Exception
        if action_name is None:
            action_name = self.generate_action_name(element, action.__qualname__)
        print(action_name)

        try:
            action(*args)
        except ElementClickInterceptedException:
            #self.browser.fullscreen_window()
            self.scroll_to_element(element)
            sleep(1)
            return self.action(action,*args, verification=verification, input_box_verification=input_box_verification, action_name=action_name, retries = retries +1)
        except ElementNotInteractableException:
            sleep(3)
            return self.action(action, *args, verification=verification, input_box_verification=input_box_verification,
                               action_name=action_name,retries = retries +1)
        except ElementNotVisibleException:
            #self.browser.fullscreen_window()
            self.scroll_to_element(element)
            sleep(1)
            return self.action(action, *args, verification=verification, input_box_verification=input_box_verification,
                               action_name=action_name, retries=retries + 1)
        except Exception as e:
            prints('failed perform %s' % action_name)
            error_msg = str(e)
            if 'Other element would receive the click' in error_msg:
                #self.browser.fullscreen_window()
                self.scroll_to_element(element)
                sleep(1)
                return self.action(action, *args, verification=verification,
                                   input_box_verification=input_box_verification, action_name=action_name,retries = retries +1)
            traceback.print_exc()
            raise

        if verification:
            success = self.verify(verification)
            if success:
                prints('successfully performed %s' % action_name)
                return True
            else:
                prints('failed to verify that we performed %s' % action_name)
                return False

        if input_box_verification is not None:
            text = args[0]
            entered_text = input_box_verification.get_attribute('value')
            if entered_text != text:
                prints('tried perform %s but text is not entered' % action_name)
                raise
            else:
                prints('successfully performed %s' % action_name)
                return True

    def find(self,type=None, text=None, verification = None):
        # if verification is given, type and text param wont be used
        # return: Bool, Selenium Element.
        # since new selenium seems to throw error when element is not found, catch error and return false when element not found
        try:
            if verification:
                type = verification.type
                text = verification.text
                self.verify(verification)
            prints('finding element %s by %s' % (text, type))
            func = self.types[type]
            element = func(text)
            self.current_element=element
            return element, element
        except NoSuchElementException:
            prints('failed to find elment %s by %s' % (text, type))
            return False, None
        except Exception as e:
            traceback.print_exc()
            return False, None



# EXAMPLES:
if __name__ == "__main__":
    test=Bot('./chromedriver.exe')

    # logger use example
    test.set_logger('logs.txt')

    v1 = Verification(type='xpath',text='/html/body/div[2]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button')

    test.enable_network_logs()
    test.visit_site('https://www.nike.com/ca/launch', verification=v1)


    # how to perform actions
    # this find() uses string input
    success, login_button = test.find('xpath', '/html/body/div[2]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button')
    v2 = Verification(type='xpath', text='//*[@placeholder="Email address"]')
    test.action(login_button.click, verification=v2, action_name='pressing log in button')

    # save time by using pre-defined verfication as input, find() will ignore first two params so just put whatever
    success, email_box = test.find(verification=v2)
    test.action(email_box.send_keys, 'email@mail.com')
