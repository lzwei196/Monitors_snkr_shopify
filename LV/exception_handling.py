from LV.web_elements import *
from selenium.common.exceptions import *
from util.ansi_colour import *
from selenium_wrapper.bot import MAX_RETRY

class UnavailableException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def handle_atc(self):
    msg = magenta(f'Place to Cart not available.....but was unable to pin point the exact error')
    verifications=[v_cfa,v_out_of_stock,v_status_500, v_notify_me, v_call_for_ava]
    for verification in verifications:
        element = has_element(self, verification)
        if element is False:
            continue
        else:
            text = element.text
            if text == '':
                text = verification.text
            msg = magenta(f'Place to Cart not available, only have {text}"')
            if verification == v_status_500:
                pass
                #todo do refresh and retries here
    update_summary(self,msg)
    raise UnavailableException(msg)


def has_element(self, verification):
    try:
        return self.find(verification=verification, retries=MAX_RETRY-1)
    except NoSuchElementException:
        return False

def update_summary(self, reason):
    if self.product_url in self.summary:
        nested_dict = self.summary[self.product_url]
        if reason in nested_dict:
            nested_dict[reason] += 1
        else:
            nested_dict[reason] = 1
    else:
        self.summary[self.product_url] = {reason: 1}

def error_handler(f):
    def handler(*args, **kw):
        self = args[0]
        try:
            result = f(*args, **kw)
            return result
        except:
            if f.__name__ == 'atc':
                handle_atc(self)
            else:
                update_summary(self, f.__name__)

    return handler

# @error_handler
# def test(a, b, c, keyarg=0):
#     a = {}
#     b = a['test']
#
# test(1,1,1)