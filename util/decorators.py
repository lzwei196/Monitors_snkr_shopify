import time
import traceback
import requests

debug_mode=True

def timer(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        # print ('func:%r args:[%r, %r] took: %2.4f sec' % \
        #   (f.__name__, args, kw, te-ts))
        msg = 'func:%r took: %2.4f sec' % \
          (f.__name__, te-ts)
        print(f'\033[35m{msg}\033[0m')
        return result
    return timed

def debug(f):
    def timed(*args, **kw):
        name = f.__name__
        self = args[0]
        if "__" in name:
            name = str(self.__class__) + f.__name__
        print('\nentering',name )
        try:
            result = f(*args, **kw)
        except:
            print(f.__name__, "failed with args: ", *args, kw)
            #traceback.print_exc()
            raise
        print('\nexiting', name, '\n\n')
        return result
    return timed

def exception_handler(f):
    def handler(*args, **kw):
        self = args[0]
        try:
            result = f(*args, **kw)
        except requests.exceptions.ConnectTimeout:
            print('connect timeout, resetting cookies')
            self.set_cookies()
            print('retrying ', f.__name__)
            return handler(*args, **kw)
        except requests.exceptions.ReadTimeout:
            print('read timeout, resetting cookies')
            self.set_cookies()
            print('retrying ', f.__name__)
            return handler(*args, **kw)
        except KeyError:
            print('likely response had no key "id" in json, but might be caused by something else')
            traceback.print_exc()
            print('retrying ', f.__name__)
            return handler(*args, **kw)
        except:
            traceback.print_exc()
            raise
        return result
    return handler

def exception_handler_LV(f):
    def handler(*args, **kw):
        self = args[0]
        try:
            result = f(*args, **kw)
        except requests.exceptions.ConnectTimeout:
            print('connect timeout, sending out alert anyways')
            # self.set_cookies()
            # print('retrying ', f.__name__)
            # return handler(*args, **kw)
        except requests.exceptions.ReadTimeout:
            print('read timeout, sending out alert anyways')
            # self.set_cookies()
            # print('retrying ', f.__name__)
            # return handler(*args, **kw)
        except KeyError:
            print('likely response had no key "id" in json, but might be caused by something else')
            traceback.print_exc()
            # print('retrying ', f.__name__)
            # return handler(*args, **kw)
        except:
            traceback.print_exc()
            raise
        return result
    return handler

# @debug
# def test(a, b, c, keyarg=0):
#     a = {}
#     b = a['test']

