from requests_html import HTMLSession

class Requests_bot():

    def __init__(self):
        self.session = HTMLSession()

    def get(self, url, **kwargs):
        print(f'sending request to {url}')
        response = self.session.get(url, **kwargs)
        print(response, url)
        return response

    def post(self, url, **kwargs):
        print(f'sending request to {url}')
        response = self.session.post(url, **kwargs)
        print(response, url)
        return response

    def put(self, url, **kwargs):
        print(f'sending request to {url}')
        response = self.session.put(url, **kwargs)
        print(response, url)
        return response

    def options(self, url, **kwargs):
        print(f'sending request to {url}')
        response = self.session.options(url, **kwargs)
        print(response, url)
        return response