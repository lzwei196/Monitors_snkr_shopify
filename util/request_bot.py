from requests_html import HTMLSession
import requests_html


class MethodDoesNotExist(Exception):
    pass

class StatusCodeAbove400(Exception):
    pass


class Requests_bot():


    def __init__(self, TIMEOUT=30):
        self.session = HTMLSession()
        self.REQUEST_METHOD = {'get': self.session.get,
                               'post': self.session.post,
                               'options': self.session.options,
                               'put': self.session.put}
        self.TIMEOUT=TIMEOUT

    def request(self, method, url, **kwargs):
        try:
            if 'timeout' not in kwargs:
                kwargs['timeout'] = self.TIMEOUT
            print(f'sending {method} request to {url}')
            function = self.REQUEST_METHOD[method]
            response = function(url, **kwargs)
            print(response, url)
            if response.status_code >=400:
                print(response.text)
                raise StatusCodeAbove400
            return response
        except KeyError:
            print(f'unsupported method {method}')
            raise MethodDoesNotExist

    def get(self, url, **kwargs):
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('post', url, **kwargs)

    def put(self, url, **kwargs):
        return self.request('put', url, **kwargs)

    def options(self, url, **kwargs):
        return self.request('options', url, **kwargs)