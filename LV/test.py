from pprint import pprint
from selenium_wrapper.selenium_support import *
import platform
sample = {"addressInfo":[{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G0E1","phone":4387258504,"saveToProfile":True,"country":"CA","locationId":None,"overrideAddressVerification":False,"suggestedAddress":{"addressLine1":"1510-1450 boul René-Lévesque O","addressLine2":"","city":"MONTRÉAL","state":"QC","postalCode":"H3G 0E1","country":"CANADA","poBox":"","generalDelivery":"","routeService":"","buildingName":"Yul Tour 1","largeVolRecieverName":"","verificationLevel":"VERIFIED","addressType":"letterCarrier"}}]}


sample2 = 'lvbmwe1=55AF2AF22430C80C2FE8EF1C1645450C; lv-dispatch=eng-ca; lvbmwe2=A3CCD2826076546410DC8A7F94574D3A; ATGID=anonymous; SGID=sb.springboot31-prd; storeLangCommerceHeader=eng-ca; ak_bmsc=E210B454A863082CE6188D6AF4088DFE173B9AC541750000FF8FD45FEF86033A~plPnw707/aPYjtts1pffimqOpukcLvO1HtR5jjUBo08TTbO5WDPwIWdJXssw3KVtmQukfvW/EtdeE3ESljJ6BdfI4fYgm/bcF5yMMhiRGaBuMk4V7FYI1MaEyqE4tctBOyJ0oTyrjlqmIuPm2zYXiLqJJUCu96unsWBqZnRIxX+03FnwE2FMfqP9xdwYOU4G31mHS9h1qb0COrnTvH5LgN4lrEQ+9tvu6DD/QwJdYh3HcFEhLR8qJ6Fb+wVHLY5ujltPtiNVGaI0CoAbMef3DbUg==; bm_sz=EE5344C00DC003C731F452B0263872A2~YAAQxZo7F0CWKJV1AQAAsn9SVgrykgH0kQZr7HmiYCqfhjoQT9ZXEl7NqgpN0QGsW6AOraD9D0RSn71423wucsROBD4p7UosxNEogmB535dH59r9BXoHeXJwD21RUwY9c4fk8CHqeI36aRI0KQRv+wao8ZYE0yGYwSL2uBNJLZq4w0hhK+bD94WrqNh/1fFs3bKxRAie; _dynSessConf=8538336961660798145; AKA_A2=A; ATG_SESSION_ID=4W8RUhH5-XpxX3pUSyljx7ji.front31-prd; JSESSIONID=4W8RUhH5-XpxX3pUSyljx7ji.front31-prd; lv-dispatch-url=https://ca.louisvuitton.com/eng-ca/products/game-on-classic-bikini-bottoms-nvprod2550060v#1A8LX4; order_CA="H4sIAAAAAAAAAKtWyi9KSS1SslLKqzAyNDA0NTEyNVSqBQAJQwc7FwAAAA=="; orderSize_CA=2; lvbmwe1=44C33110FCB654FA0883CCF8B50583C0; bm_mi=38F1CC2CE53F89CFFDFAE0CF68CCB64E~eV01UK+y7KTC5IWkJkCYnfg6QxxDChkt0OrjhYmGOOzjmeUccF4dykAEEUOsH3AcRkITKQG091gX3smhDKBRHTk75Krjhp05450OZHCjrNshxfjWHhkKcFeO4jt+wFNl40y0m2KJkiEke8mMVKOtUET4cbYXTO8sEGGvt0HUhPcCM+XWznoxXG3Z+3slZgE9Otk/61ROxGBbRDIT0yDlOtGU5NlLfhb8m2aS9PIyiKBer+Ymml/5hqmJPRacl6Ov; bm_sv=61558FDCB9A7EEB4BBE97DC30E317D06~XfQRMDRTn9b+5cJd40XUCCh2XFrGs7hS9oVrfXqprQkKJaErzw5e2lhvLoL3O2aCw8dCKnIJeTHhOQ8LJwxJK1NChD/as658A2R250Y7nqwXGgfX+6n6Ri3Ut3bWoKDulPYKyhrTcLCA0fUSdDGieSxeaSceEonqOzeUUDTCEIw=; _abck=82085626A5A176E110C0DBF9D25C9FF8~0~YAAQrJo7F90of6F1AQAA5y5nVgVkwp3j2iCS6oJyywrqMVAKFiBWah59cBb45x4B4g1BTwVHvSZZFoaZM0Qp/29nw1XqypqstOJsjZHwXMWLmGtTxqx1LAUQ177c5h/faXwz+CaSALIxXAVcdOSMMOHQenUEN2E/l6yUtq8BgI+zYUQ9IX3jTEZrxvQkutjqjrGCwqspoHth0KisigHnjW+ecI1xuxJqOeQPK6oQ+a2mQfJgJk7rXUxFppDHQC/JN56Ol+JzGJPmkWEXlm/rq587uJzUYWh1ntUg1O8UJ3TnuX239yGT4m03q/T0guRkWgxoSqcA+ALtwdCKxC8uOMQ66IQC5BdGocWulg==~-1~-1~-1; prevURL=https://secure.louisvuitton.com/eng-ca/checkout/shipping; currentURL=https://secure.louisvuitton.com/eng-ca/cart; ak_wfSession=1607769171~id=DIF+IYTNwGaMJOf/tq5+9c6rfK0DJh+4fcJ2TUkyLN4='
def func(json):
    for k, v in json.items():
        if type(v) == ''.__class__:
            print('%s="%s"' % (k,v))
        elif type(v) == {}.__class__:
            func(v)
        else:
            for item in v:
                func(item)

def cookie_format(string):
    cookies = {}
    string = string.split('; ')
    for item in string:
        item = item.split('=')
        cookies[item[0]]=item[1]
    return cookies

# pprint(cookie_format(sample2))

print(platform.system())





