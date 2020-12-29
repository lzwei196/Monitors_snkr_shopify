from pprint import pprint

sample = {"addressInfo":[{"firstName":"ziwei","lastName":"li","addressLine1":"1510-1450 Boul René-Lévesque O","addressLine2":"","city":"Montréal","state":"QC","postalCode":"H3G0E1","phone":4387258504,"saveToProfile":True,"country":"CA","locationId":None,"overrideAddressVerification":False,"suggestedAddress":{"addressLine1":"1510-1450 boul René-Lévesque O","addressLine2":"","city":"MONTRÉAL","state":"QC","postalCode":"H3G 0E1","country":"CANADA","poBox":"","generalDelivery":"","routeService":"","buildingName":"Yul Tour 1","largeVolRecieverName":"","verificationLevel":"VERIFIED","addressType":"letterCarrier"}}]}


sample2 = 'GB_test=groupby; AMCVS_D6E638125859683E0A495D2D%40AdobeOrg=1; ai_user=yI5IYHrdaELdeNJVDrjjgr|2020-11-06T00:16:28.046Z; clientId=LiiKlZSJL71UfyBU; dtCookie=1$9F8477507D18E4BF7DF9A6CEC92B6DEC; criteoVisitorId=f58248bb-eb83-46a1-a758-46780f9bf5d7; enabled=1; ReturnUrl=https://www.bestbuy.ca/; surveyOptOut=1; BVImplmain_site=18193; CS_Culture=en-CA; lastUsedLocations=%7b%22shippingLocation%22%3a%7b%22city%22%3a%22Burnaby%22%2c%22postalCode%22%3a%22V5C%22%2c%22region%22%3a%22BC%22%7d%2c%22pickupLocation%22%3a%7b%22city%22%3a%22Burnaby%22%2c%22postalCode%22%3a%22V5C%22%2c%22region%22%3a%22BC%22%7d%7d; tx=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhODA5MTVjNy0xMzViLTQwMTgtODU3Ny1kYjcyZTRjODFiN2QifQ.6Knq7yiztHyqpf8hcZymMM_Ij0n_oq1kiUU4j6I4DvM; b6bab32db12a74433294191e1fddb23a=a830c713609836df4de07e88cf059364; _abck=7C171628E453FD33CC5671AF6B56668F~0~YAAQZ8fCzwEwHXh1AQAAo/+jBwT18MM61yjAwi0OnKbslsZDIAOB4DC/vld7238oxVvDmsFByxu7TEWQjAYpeFmNQMBZnfG7pWda7lP1ChLVeYg5b+n2Yqr3VraU/ben8psRi3FExLOd4/jp1WkvldMYQbbpz89kvPBg6tNdJNHww0fPSc7zDQPP8Z2UDX+L52xbblv4Huyaux2YK/Qkz7naxII9i3Ib/kW0uZ/3Zi515wsD0E6Ry2R6whiEAW3SkP/RXyHEtccBT765/+p7OyeQiID7kJvYrhGML3iji1ZL4DLVQH8kiy1VyH2gGXpGqxHb+9sdoJldRx1TqAaMQvkyVZNHAQ==~-1~-1~-1; ak_bmsc=AABB5DBC1FE5615EF739081A17D66E85CFC2C7759E7D00005153C85F0F2E8F35~plpudJFB3AY+nbf6qq771+pXrsABlROD3giKiFi8mGj60iY+qJM0sSng3YUMEixZox+h3CRAnP6V32TwaN59FY4XGxH+4SZw8w44N6di7cbOO63k9x+sw1woz9etYRB/vg4Xj8bgxHHEwH+5x/IAmpY/YQcceNpkVqL7KVZ5YrZNn1fvkXNLVY4K1cKgOmDcOE3veK2mzPY3JE71wnQoy1qLM5RqC/imx3NNYzcIoFvnI=; bm_sz=BDE5704FB29F89A2005B98EF5D38B2F8~YAAQdcfCz38yN6B1AQAAi3eFJgnC0MvC+07ceYjs0dfDSLiFudyvuGCr+TcZOCwAaaNCwXdtEBFZBzsTT5Tv76lR57yUtHPIU80SK79uZO7tInpMVQKtj/bM84EfPFcpMnzaKfUuxBxyhov3gAoJU5co/M5KB3TO6D3aK0iSUfCM92nokcRsF1d+0FNe9HlQ; ai_session=dxfNHrLs+5dzBU/LNDSxP7|1606964052037|1606964052037; AMCV_D6E638125859683E0A495D2D%40AdobeOrg=-1303530583%7CMCIDTS%7C18600%7CMCMID%7C05633117643816212064333719072983066662%7CMCAID%7CNONE%7CMCOPTOUT-1606971252s%7CNONE%7CvVersion%7C3.3.0; mbox=session#73707aea36b64bbe94fb0710f2036050#1606965913; QueueITAccepted-SDFrts345E-V3_prebf012020browse=EventId%3Dprebf012020browse%26QueueId%3D13bb5b90-ac1a-4d14-816e-f1f096503f1b%26RedirectType%3Dsafetynet%26IssueTime%3D1606964054%26Hash%3D62aaa137df6204f182b608c748c530eba004223ed4f606e47bbef62c005ec5ee; nps={"currentUrlPath":"/en-ca/basket","hasSurveyBeenDisplayed":false,"heartBeat":1606964114,"isInSampling":false,"pageViewCount":4,"surveyLastDisplayed":1636157788}; fdb7491a5cc3d693edd0926b3a48659f=7a25fea30584ebae7a2dc8e3291c9700; bm_mi=D9A6146B47B715E82FF6AD8586A1E288~pcGkerVVvZ02zrP2fza9Uwd7itYhI8vmuCrMweoKwPbOVtIvo0NBMshcylpMI7wEAdoClEeJYOyiRVKfjJLPTKQaWx02CMKk/J+xuGB//ROK7OamoZNfqz/xEc9afMv+n1odgUdHoqiiFxRZdJQzagBXrdJArEMCOsTDnc2QWPH1nE+T1wq12u066YQ4SRQkJJ9Shx/zkguQQa2/3te8J+4Gx8dPVFR8C/huQKFN7I/1mrpgJ63f38akN110RMnt; 47236a0d189c10314faac13e28785259=84bc83eb749a1707b4bcc3c9d560bef2; QueueITAccepted-SDFrts345E-V3_prebf012020checkout=EventId%3Dprebf012020checkout%26QueueId%3Daedd6e9e-9f34-4be8-8fd9-f1f244b37089%26RedirectType%3Dsafetynet%26IssueTime%3D1606964135%26Hash%3D4112dfc57abbc771857735439e54d6d23cd9e2acb99ebc94e9a6c91e76926810; bm_sv=46E329B5119920A80E9A60FD6E6243DB~7E5kTBui4TPEDoV1aeAvVMw4ddNxD4ubSRvdYK2NoGquV8ggxqpjEXO7foHbfMCC7Gh2zC7CwuLC2h+bP52Tv1AocKdcUdi5Fr4j/mUvx2DMf1j2IZazgwDJ/roAVy/ZnxLoIPMPguIGreoEPGosUAMlGqLw6igjd2V1Ndn2OYE=; cartId=ed439d22-ee5f-4803-ac8b-e8fcd62dc99c'


walmart_payment ='headerType=whiteGM; ENV=ak-scus-t1-prod; vtc=VcvnST7e2GQ6MTiak_WeFQ; bstc=VcvnST7e2GQ6MTiak_WeFQ; TS0196c61b=01538efd7ce5d709d07a042b6818af85425ad723b3dd96dfa5b382c4dc72fcf5a1ca833a2785b10dd49960e09776e85a1e4815d8d8; TS017d5bf6=01538efd7ce5d709d07a042b6818af85425ad723b3dd96dfa5b382c4dc72fcf5a1ca833a2785b10dd49960e09776e85a1e4815d8d8; userSegment=40-percent; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; _ga=GA1.2.2104260021.1606969460; _gid=GA1.2.8386757.1606969460; s_vi=[CS]v1|2FE4343A0515B1D0-600007B7B071B750[CE]; s_ecid=MCMID%7C90701947545167018113634014970567527942; walmart.id=23103eb9-5686-4a75-8e3d-854e6f66da82; _fbp=fb.1.1606969460340.1764223031; _pxvid=6a3c839f-351f-11eb-94cc-0242ac120017; xpa=1kb5h|2lwWQ|63K3S|7Xi3l|DViIf|DwTRU|GpBCe|HbOxV|Jeavw|LVSOt|MBc1l|MZ9tt|NOaJP|Oqgc1|Q0IHr|X92ox|YJsua|_vY-K|a4vv4|dykD1|fHfTr|fJumS|hcz5Y|jeBOs|lZnE7|mOlOu|rwaVg|sGGbM|wM_1h|wx8xe|yI7_k; exp-ck=1kb5h17Xi3l1DwTRU1GpBCe1HbOxV1Jeavw1MZ9tt1Oqgc14X92ox4YJsua5a4vv41dykD11fHfTr2fJumS3lZnE76rwaVg4sGGbM4wM_1h1wx8xe1yI7_k1; TS01170c9f=01538efd7ce5d709d07a042b6818af85425ad723b3dd96dfa5b382c4dc72fcf5a1ca833a2785b10dd49960e09776e85a1e4815d8d8; _gcl_au=1.1.683101946.1606969460; DYN_USER_ID=a26645f5-f6da-412c-b0f7-eddbe5ab1155; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE43beqZq1zoARAXj2E9y3/SF72xqpoSeMrFuXCRh+ib2VgJFMtaGBSY3IGtClJoEPsUBdvEoO+zpmuj01Iz7EPmhW0ZRVbziguJ3FQieLTiJAMbR6W/1p270az/qEhDhqvj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj1DKCLKGCHSNWnjvlrwPU+r50BU6bog5uV5iVhBsfrYDLEjvN5FvWr04fgKYbVEcPPb/SoGFgAYL9DGZ8K45WCXb/Ew67/GsLtdlJHpe1JgEIJ5C6OcCFiwazvf7DdUJGkc8IAFKTMeYOPXxSWUpSrKUrWWeePqEK2nLgTCIZeKJb+Ew6FVwCF83dZ1EvvfqJ4Q/NZu0iLYP9wT2tuX28y44vwKpAKCaQC31wImMq3GDQ==; LT=1606969460848; WM.USER_STATE=GUEST|Guest; s_visit=1; s_cc=true; xpm=1%2B1606969460%2BVcvnST7e2GQ6MTiak_WeFQ~%2B0; wmt.breakpoint=d; walmart.csrf=9347f0d1279871698a7fd47d; DYN_USER_ID.ro=a26645f5-f6da-412c-b0f7-eddbe5ab11'

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

cookies1 = cookie_format(sample2)


from sites.bestbuy_bot.bestbuy_bot_working import bestbuy

bestbuy = bestbuy()
bestbuy.start_bot()
cookies = bestbuy.session.cookies



for name, val in cookies.items():
    #print(cookie['name'], cookie['value'])
    if name in cookies1:
        print('deleted a cookie')
        del cookies1[name]

print('leftover cookies')
pprint(cookies1)




