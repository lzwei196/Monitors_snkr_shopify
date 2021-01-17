import requests_html
from util.ansi_colour import *
from time import sleep
from requests.exceptions import *
from urllib3.exceptions import *
import sys


class MethodDoesNotExist(Exception):
    def __init__(self, existing_methods):
        super().__init__(f'currently there are these methods: \n {existing_methods}')

class StatusCodeAbove400(Exception):
    def __init__(self, response, message='this outgoing request received a status > 400'):
        super().__init__(message)
        self.response = response

class MaxRetryReached(Exception):
    def __init__(self, url, message=None):
        if message is None:
            message = f'max retry reached when trying to connect to {url}'
        super().__init__(message)


#just a wrapper for requests that will auto print some debug stuff

WAIT_TIME=10
MAX_RETRY=10

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
            print(self.ignored_exceptions[exception])
        else:
            raise exception

    def ignore_VPN_exceptions(self):
        self.add_exception(ConnectionError)
        self.add_exception(MaxRetryError)
        self.add_exception(NewConnectionError)
        self.add_exception(ConnectionAbortedError)

    def request(self, method, url, retries=0, **kwargs):
        if retries > MAX_RETRY:
            raise MaxRetryReached(url)
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
            raise MethodDoesNotExist(self.REQUEST_METHOD)
        except BaseException:
            exception = sys.exc_info()[0]
            self.handle_exceptions(exception)
            sleep(WAIT_TIME)
            return self.request(method, url, **kwargs)

    def get(self, url, **kwargs):
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('post', url, **kwargs)

    def put(self, url, **kwargs):
        return self.request('put', url, **kwargs)

    def options(self, url, **kwargs):
        return self.request('options', url, **kwargs)


if __name__ =='__main__':
    import requests.exceptions
    import urllib3.exceptions

    session = Requests_bot()
    session.add_exception(requests.exceptions.ConnectionError)
    session.add_exception(urllib3.exceptions.MaxRetryError)
    session.add_exception(urllib3.exceptions.NewConnectionError)
    session.add_exception(ConnectionAbortedError)
    session.get('https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e-in-python')