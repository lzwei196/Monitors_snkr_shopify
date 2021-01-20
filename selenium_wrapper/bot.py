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
from util.ansi_colour import *
import platform
import subprocess
import urllib3
import inspect


# import this variable when using the class Snkr
Verification = namedtuple('Verification', 'type text')
INTERNAL_LOGGING = None
VERBOSE = True
AUTO_QUIT = True
MAX_RETRY=3

class MaxRetryExceeded(Exception):
    pass

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
        self.init(driver_path,headless=headless)

    @timer
    def init(self, driver_path,headless=False):
        options = Options()
        options.headless = headless
        ##anti detection
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.browser = webdriver.Chrome(driver_path, chrome_options=options)
        self.browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        self.browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        self.headless=headless
        self.driver_path = driver_path
        # store functions in dictionaries so we can make our own find functions with error handling and logs
        # todo, incompleted list of functions
        self.types={'class': self.browser.find_element_by_class_name,
                    'css':self.browser.find_element_by_css_selector,
                   'xpath': self.browser.find_element_by_xpath,
                    'id': self.browser.find_element_by_id,
                    'tagName': self.browser.find_element_by_tag_name}
        #simmilar idea as above
        # todo, incompleted list of By types
        self.verification_types={'xpath': By.XPATH}
        self.action_ctx=[]
        prints('finished init with', driver_path)

    def restart(self):
        print('resetting chromedriver')
        self.clean_up()
        self.init(self.driver_path, headless=self.headless)

    def clean_up(self):
        if self.browser is None:
            print('skipping clean_up')
            return
        print('CLEANING UP SELENIUM')
        try:
            self.browser.close()
            sleep(3)
            self.browser.quit()
            self.browser=None
            if platform.system() == "Windows":
                stdout = subprocess.check_output("taskkill /im chromedriver.exe /f", shell=True).decode()
                print(stdout)
            else:
                #this is specific to my setup, if u use ur linux host for other stuff u will need a better cleanup cmd
                stdout = subprocess.check_output(f"pkill -f chrome", shell=True).decode() #kill all chrome process
                print(stdout)
        except subprocess.CalledProcessError as grepexc:
            if grepexc.returncode in [128, -15]:
                print('no chromedriver proccess was running')
            else:
                print(f'failed to clean up chromedriver {grepexc.returncode}')
                #traceback.print_exc()
        except urllib3.exceptions.MaxRetryError as e:
            print('an attemt shutdown chromedriver when it is already closed')

    def __del__(self):
        if AUTO_QUIT is True or self.headless is True:
            self.clean_up()

    def save_page(self, file, retries=0):
        print(f'saving page to {file}')
        try:
            html = self.browser.page_source
            with open(file, 'w', encoding='utf-8') as fout:
                if len(html) >8:
                    fout.write(html)
                    return html
                else:
                    print(f'page source empty, retrying {retries}')
                    sleep(2)
                    return self.save_page(file, retries=retries+1)
        except:
            print('failed to save page')
            traceback.print_exc()

    def press_key(self, key, verification=None, retries=0):
        if verification:
            success = self.verify(verification)
            if success:
                prints(f'successfully pressed {key} {retries} times and {verification.text} became clickable')
                return True
            else:
                prints(f'tried to press {key} but the element {verification.text} is still unclickable, retying...' )
                self.press_key( key, verification=verification, retries=retries+1)

        actions = ActionChains(self.browser)
        actions.send_keys(key)
        actions.perform()

        if retries > MAX_RETRY:
            raise


    def scroll_to_element(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def scroll_to_element_and_click(self, element):
        actions = ActionChains(self.browser)
        hover = actions.move_to_element(element)
        hover.click().perform()

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
            #todo
            self.action_ctx.append('timed out waiting for element %s to show up' % text)
            return False
        except Exception as e:
            self.action_ctx.append(red(e))
            return False

    def generate_action_name(self, element, act):
        try:
            name = element.get_attribute('name')
            id = element.get_attribute('id')
            class_ = element.get_attribute('class')
            arr = [name, id, class_]
            for item in arr:
                if item is not None and item != '':
                    return '%s on %s' % (act, item)
            return '%s on %s' % (act, 'unknown element')
        except:
            return '%s on %s' % (act, 'unknown element')

    def print_ctx(self,ctx):
        msg = '\n    '.join(ctx)
        print(msg)

    @timer
    def action(self, action, *args, verification=None, input_box_verification = None, action_name=None, retries = 0):
        #if input_box_verification is passed auto check if text is entered
        if self.current_url != self.browser.current_url:
            self.current_url = self.browser.current_url
            print('URL:', self.browser.current_url)
        wait_time=3
        element = action.__self__
        if retries >MAX_RETRY:
            #traceback.print_exc()
            self.action_ctx.append(red(f'FAILED to perform {action_name} after {retries + 1} tries'))
            self.action_ctx.append(f'last know exception: {self.last_exception}')
            self.print_ctx(self.action_ctx)
            raise MaxRetryExceeded
        if action_name is None:
            action_name = self.generate_action_name(element, action.__qualname__)
        if retries == 0:
            self.action_ctx=[f'    Action Log : {action_name}', ]
        try:
            action(*args)
        except (ElementClickInterceptedException, ElementNotVisibleException, ElementNotInteractableException) as e:
            self.last_exception=e
            sleep(wait_time)
            return self.action(action,*args, verification=verification, input_box_verification=input_box_verification, action_name=action_name, retries = retries +1)
        except (StaleElementReferenceException) as e:
            self.last_exception = e
            sleep(wait_time)
            return self.action(action, *args, verification=verification, input_box_verification=input_box_verification,
                               action_name=action_name,retries = retries +1)
        except Exception as e:
            self.last_exception = e
            error_msg = str(e)
            if 'Other element would receive the click' in error_msg:
                #self.browser.fullscreen_window()
                self.scroll_to_element(element)
                sleep(wait_time)
                return self.action(action, *args, verification=verification,
                                   input_box_verification=input_box_verification, action_name=action_name,retries = retries +1)
            else:
                self.action_ctx.append(red(f'failed perform {action_name} after {retries + 1} tries with exception: {e}'))
                self.print_ctx(self.action_ctx)
                raise

        if verification:
            # todo add a fail element (where if the element is found return fail right away)
            success = self.verify(verification)
            if success:
                prints(green(f'successfully performed {action_name} after {retries +1} tried'))
                return True
            else:
                #prints('failed to verify that we performed %s' % action_name)
                sleep(wait_time)
                self.action(action, *args, verification=verification, input_box_verification=input_box_verification, action_name=action_name, retries=retries+1)
                return False

        if input_box_verification is True:
            text = args[0]
            entered_text = element.get_attribute('value')
            if entered_text != text:
                self.action_ctx.append('tried perform %s but text is not entered, clearing and retrying...' % action_name)
                element.clear()
                self.action(action, *args, verification=verification, input_box_verification=input_box_verification,
                            action_name=action_name, retries=retries + 1)
                raise
            else:
                prints(green(f'successfully performed {action_name} after {retries + 1} tried'))
                return True
    @timer
    def find(self,type=None, text=None, verification=None, retries=0):
        # if verification is given, type and text param wont be used
        # return: Bool, Selenium Element.
        # since new selenium seems to throw error when element is not found, catch error and return false when element not found
        try:
            if verification:
                type = verification.type
                text = verification.text
                self.verify(verification)
            # if retries==0:
            #     prints('finding element %s by %s' % (text, type))
            func = self.types[type]
            element = func(text)
            self.current_element=element
            return element
        except NoSuchElementException:
            if retries>=MAX_RETRY:
                prints(f'failed to find elment {text} by {type} after {retries+1} tries')
                raise
            else:
                return self.find(type=type, text=text, verification=verification, retries=retries+1)
        except Exception as e:
            #traceback.print_exc()
            raise e



# EXAMPLES:
if __name__ == "__main__":
    test=Bot('../chromedriver.exe')
    test.clean_up()
    exit(0)
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
