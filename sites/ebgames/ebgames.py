from requests_html import HTMLSession
import json
import datetime
import time
import selenium_wrapper.selenium_support as ss
from util.decorators import *
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52',
     'origin':'https://www.ebgames.ca',
    'accpet':'*/*',
    'accept-encoding': 'gzip, deflate, br',
    'referer': 'https://www.ebgames.ca/Home/Index',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'x-newrelic-id': 'Vw4FUFNRGwEEVlVTAwEF',
    'x-requested-with': 'XMLHttpRequest',
          'content-length': '0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'prefer': 'safe',
    'cookie':
            '__zlcmid=10xjYHa5kn9wXvt; .ASPXANONYMOUS=5RN0mP3Qt38jvm3iWjjvb_xA8DmZki6r3xMufLcqlzmCtcHQfY6gs1Zv4V620F_-yjU9pEozI_HZg1kH4WmZrqBGNRMvUz3t35e_P-cVIfifv6kqFDvkH79P3BysCOsmEz--WQ2; __auc=2e7de83117602fb02ab56938529; _ga=GA1.2.158343441.1606367773; com.silverpop.iMAWebCookie=e0c81a33-4591-4a35-6182-ac630a92c11c; ak_bmsc=6A252D52B4D77EB0C03C49C4BCE4FC18ACE814C4B6430000B106C85F814C2E4D~plaouWD6H2SanOHrI2Nh0Ecj7jJ5ntCPkJHynHByw01D3Gf2nmr5LhQRq4HmTAQVGi8T0QBoYqg4UO6OSm8JAFowupYEou8x40rUtVknyupjhVwBzMg4u5K/kjJakKH++cd9yP6NTaGjSo8IEwzcrajVgT+x59xJ/W5+pvM2yQ8RYuHAc7Q7fle1U3ggOHSRTKVLjH6Ix9V5DD+qkd7qFm9PHvXZ/KhP7DbpgZ9tBsggg=; bm_sz=A210E72C6A360CF2F055DF74601296DD~YAAQxBTorBz9Bx92AQAAfSRaJQkgY3uS1/ldczo1VK7BzXeaqkhAAzGogTZSvls3OVLWvkicJbyuMesgLwGlDDzWCjRpk6tGQD5Icj6F9G+59tra1GT3nG/a1kprWUdJLm6bia5j8/Fi+eaR3a3KRt25t7v8f1jPKyI1F5duu+gZowdoee5GTJNgQ9qoet+O; _gid=GA1.2.245867723.1606944434; __asc=acbb257e176255a27b5c9909348; com.silverpop.iMA.session=aa6c8610-44c2-62e0-aaa6-586134c90019; _dc_gtm_UA-135210032-2=1; _gat_UA-135210032-2=1; RT="z=1&dm=ebgames.ca&si=8x0otyfq8ob&ss=khydwa5o&sl=0&tt=0"; mp_ebgames_ca_mixpanel=%7B%22distinct_id%22%3A%20%2217602fb01081f7-073a66fdf8a4a3-5a30124a-480000-17602fb0109cc2%22%2C%22bc_persist_updated%22%3A%201606945735244%2C%22language%22%3A%20%22en%22%7D; com.silverpop.iMA.page_visit=-1032700655:-433423622:; AWSALB=TP/4+igP0MfjrqgPEQAT9/hmW9HmiNbNXulw8aQeJytfGmH4hQLvQ2ym9Dc44AkO0yJhJJpDCSgCoSg3ooACHGBHp21PsxNy061kYO0KHHPPox+dUapgxzdxsw9K; AWSALBCORS=TP/4+igP0MfjrqgPEQAT9/hmW9HmiNbNXulw8aQeJytfGmH4hQLvQ2ym9Dc44AkO0yJhJJpDCSgCoSg3ooACHGBHp21PsxNy061kYO0KHHPPox+dUapgxzdxsw9K; akavpau_Prioritization=1606946341~id=17859a49ac4c5fe33fd696606ab7b6b2; bm_sv=3C1116CD171FB7625E5C3AA2794DBD05~A00IdyCZk3FUUVcsIe5I7FNP8IZo6fr9pDz4xQxnzntjVCHv7hi5+0ykGYzPPwbfL2zO7KLMvXriPsoDeZeJhKifTN31XJAn61SMAHNYQAG+DKetUkSWU5mXh/WuiY8t4qYFOOOVHEYkembzOAoqMwpu3LfztNu8BGbl+Tjl4YQ=; _abck=FC578C17A9D6D3830F1F5E982196F834~0~YAAQxBTorFXhCR92AQAAdxpuJQS+/AJWw5vwTDrRb1xmYb5ncDsfRQl6va28ADljGg/SnTSHojwo+Iqboafkpx6TiDLuz21ywcCy0O42VNEB653mm9C7/6BOJ6LwexNvHbqq9XW8dYPrm3R8sG8IhFaHhGA5NjTpfP3gGWK9qU1CZue3KJhrMU4VWHfYSA5nCTULslf/LYouRfmeqWd4dO4ZHeN7I60oz3shK9ZciOmvS+1hAKvWvGRLDR9F2KmZo1VHBgzgCf/SgEGorozWgyukchAhiX5FOy8T0wtm+2qGDqTJ4uJ6WE/8KnZBh/xLwHtb36x7Ov1eEF862ed0jvWT+3LP+w==~-1~-1~-1'}

class Ebgames:
    @debug
    def __init__(self):
        self.session = HTMLSession()
        self.atc()
        #self.set_cookies()
        #exit(0)
        #self.session.get(product_link)
        #self.atc()
        #self.shipping()

    def atc(self):
        headers = header
        r = self.session.get('https://www.ebgames.ca/Home/Index')
        atc_link = 'https://www.ebgames.ca/api/cart/AddProduct?pvid=102620'
        r_rtc = self.session.post(atc_link, headers=headers)
        print(r_rtc)

ebgames = Ebgames()
