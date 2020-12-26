from pprint import pprint
from selenium_wrapper.selenium_support import *
import platform
from LV.LV_main import LV_requests
sample = {"addressInfo":[{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G0E1","phone":4387258504,"saveToProfile":True,"country":"CA","locationId":None,"overrideAddressVerification":False,"suggestedAddress":{"addressLine1":"1510-1450 boul René-Lévesque O","addressLine2":"","city":"MONTRÉAL","state":"QC","postalCode":"H3G 0E1","country":"CANADA","poBox":"","generalDelivery":"","routeService":"","buildingName":"Yul Tour 1","largeVolRecieverName":"","verificationLevel":"VERIFIED","addressType":"letterCarrier"}}]}


sample2 = 'lv-dispatch=eng-ca; ak_cc=CA; lvbmwe2=A3CCD2826076546410DC8A7F94574D3A; SGID=sb.springboot31-prd; SGID=.springboot31-prd; storeLangCommerceHeader=eng-ca; geolocUserZone=noZone; bm_sz=A2FA6315668EED20E59D307D6194CAD2~YAAQ1WIjFwRrEHp2AQAAQQZhlwpsJljDahy6nc9oKGz5TFwhVFUVQ1vZY0Istg0SXtao5LGCeHzUuf5CC4x6YsUQyW8LroYuep1Z9+6/T2stqjoXQIWQ0e8Lvp4t3fSXpIsM6/qarXZ+wvUn42QVkZ+/F6fzGlS3c+/FOYaKGYhQ2zYNbIM5/jzKLsxuPyTWGCOk9rAd; order_CA="H4sIAAAAAAAAAKtWyi9KSS1SslLKqzAyMjQ1M7E0MFOqBQCIL6g3FwAAAA=="; orderSize_CA=2; bm_mi=3B58C1B4A8CDA15F7D4EC061213EC618~jpT2Ak0wXAD4i/VEiKvyTIbbJO5rV5IVp/nDkD0WPNAxCz6aY+x1PIS+OjV4LQAmmZsIQOY2fscuY3Itg2at9/IWhCNhr4GE5pcYnZL+4zNE7Ak0gG3smzMrGc1+tApQeDjKoOgifMUUzMcngDiaAivVMKwH/OfupnGJXecPV4V3Xep3+Ct500PUS0Bl1vCPFUrSOQegu0pSDJaSSzyiVN35aOVPCPOQr4ZZV+MyoJkv1Ry0kqsF6Ocqk5YQEoC+XMGRx9QqNU0Erc6D7D3JwB50u5Y7qh4szz98o/WekubW0/SGgikmn8xAYogfbMB+; bm_sv=2D8D81F4CFE6AAFF4FF3728D30683991~xMMG/lwFiHU+xsw6xv39LFptFYOKO6Kr7MhJJwxZCXxEH6qhExNbk6dzR2+mm21QKy7UGAKz9+b7FG1pBUWY0/ZW8mcJfHGXK5lrcvJcyG3aulrrwZ/gQDPzsgSgKx4L1o4/r+zMQOGl1d0vnvsin5/hz0v+6w+fcJyZWWb9eg8=; ak_bmsc=491858A1110419F1CF9AC60E6A327957172362D54F4C00008E37E55FE8D9352B~pl7bSVwBHRoUVLHG2h7c2x2F458C7rJptl64G1OFv33zpszHGjYWs4Wtp5REFYWMh0s4bXLYM2vbvH8lFitRHjmfH4I/boMxXCGkmxIg18tIiqtVN3resfU2Mdh2sq0lI+vkJxN6UVm0JXRFKTAVQ5jVjsKjwsuMeiJlUj17I/cD+6ifDBR9gNl6Nc/LsT/RAmIRjhXI9zWSYE3+kOM7MwKGbffjQymQEEZqQENiT37b4PwLVjOXRwWs7l/U3MpcMwcRy0zXrfjA5dZplFOUtXW1mpiih8P7adzUS3D/BfP+qEPa12CNf47UVHvvxH5ptuduox/sPwSlqhy8sJ/JdM2Q==; currentURL=https://secure.louisvuitton.com/eng-ca/mylv/overview; _abck=EF55B91199A7B7806FAA610A6E52FC97~0~YAAQrJo7F4l8g6F1AQAAE9hzlwXyPrP9tHMMR7ad0qLF67UI11loIOvIduxY9QRIKjmzPKBDA24b8JOvIW/FyARqr0kD1kqoy/3ziMbSA+I5MyiE2iBKfVyC0c/LiDphh2zct1/mrkx46cHubVZlnUlgyEN9nLj/Xn5D/qWBWt5KheVSM8c4J3Rhsqq5bBJ/Ld1D9ULrT7x7GhdfiLq3RWRvft6TfyinCZk0eE/8DypRseYDFrxkU9vQzvnuU7Uq1Se2zVeX5l5oY9zRGE1aEde1vv12r3Lbumx8+wi1bap8ghI/Ynt24EH+4YIGgTjNk+O/chUjrhZWR/My8OZc38RGq+rLEACUbBqxEA==~-1~||-1||~-1; ATG_SESSION_ID=yPAJeGkoVyeuFeXxg-L2Witt.front31-prd; ATGID=anonymous; prevURL=https://secure.louisvuitton.com/eng-ca/mylv/overview; lvbmwe1=DF501ACF088A750B341ADFE55EF4BCA1; lv-dispatch-url=https://ca.louisvuitton.com/eng-ca/homepage; _dynSessConf=-3957170385872747029; JSESSIONID=aJ8Qmq1kcNS-fR51WHiLwfm4.front31-prd'
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

cookie1 = cookie_format(sample2)

bot = LV_requests()
bot.set_cookies()

cookies = bot.session.cookies

for name, val in cookies.items():
    #print(cookie['name'], cookie['value'])
    if name in cookie1:
        print('deleted a cookie')
        del cookie1[name]

pprint(cookie1)


