import requests_html
from util.ansi_colour import *
from time import sleep

class MethodDoesNotExist(Exception):
    pass

class StatusCodeAbove400(Exception):
    def __init__(self, response, message='this outgoing request received a status > 400'):
        super().__init__(message)
        self.response = response

#just a wrapper for requests that will auto print some debug stuff


class Requests_bot():
    def __init__(self, TIMEOUT=30, silent=False):
        self.silent=silent
        self.session = requests_html.HTMLSession()
        self.REQUEST_METHOD = {'get': self.session.get,
                               'post': self.session.post,
                               'options': self.session.options,
                               'put': self.session.put}
        self.TIMEOUT=TIMEOUT
        self.ignored_exceptions={}

    def add_exception(self,exception, msg=None):
        # add exceptions to ignore list
        if msg == None:
            msg = yellow(f'{exception} was caught but it was on the ignore list')
        self.ignored_exceptions[exception]=msg

    def print(self,*args, **kwargs):
        if self.silent is False:
            print(*args, **kwargs)

    def handle_exceptions(self,exception):
        if exception in self.ignored_exceptions:
            self.print(self.ignored_exceptions[exception])
        else:
            raise exception

    def request(self, method, url, **kwargs):
        try:
            if 'timeout' not in kwargs:
                kwargs['timeout'] = self.TIMEOUT
            self.print(f'sending {method} request to {url}')
            function = self.REQUEST_METHOD[method]
            response = function(url, **kwargs)
            self.print(f'{green(response)} {url}')
            if response.status_code >=400:
                print(response.text)
                raise StatusCodeAbove400(response)
            return response
        except KeyError:
            print(f'unsupported method {method}')
            raise MethodDoesNotExist
        except BaseException as e:
            self.handle_exceptions(e)
            return self.request(method, url, **kwargs)

    def get(self, url, **kwargs):
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('post', url, **kwargs)

    def put(self, url, **kwargs):
        return self.request('put', url, **kwargs)

    def options(self, url, **kwargs):
        return self.request('options', url, **kwargs)

