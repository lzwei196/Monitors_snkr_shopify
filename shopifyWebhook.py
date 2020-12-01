from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep



def send_webhook(title, link, url='https://discord.com/api/webhooks/783121758105370624/EE4RP3K_kNNskk_EfwsZZvg_QCh39-35m60qiUHcAcAeZ7plgWW_GtHP66rEJtbp9h4g'):
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=title, description=link, color=242424)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc(cartList, imageUrl, Link, title, price, type='newly added'):
    sleep(0.3)

    webhook_url = 'https://discordapp.com/api/webhooks/558102754107850772/6EAMHz1EuKyN2428spOpCT6WgdBDuGzp2Vk46428nvfuxkY9Dn7Fg-mXZ9_WwpZd5PRx'
   # if (carts == 1):

    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title=title, description=Link, color=242424)
    if(imageUrl != 'no image available'):
        embed.set_thumbnail(url=imageUrl)
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='type:', value=type)
    for cart in cartList:
        cartLink = cart['cartLink']
        embed.add_embed_field(name=cart['size'], value=(
            '[link]' + '(' + cart['cartLink']+')'))
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_key(cartList, imageUrl, Link, title, price, type='newly added'):
    sleep(0.3)

    webhook_url = 'https://discordapp.com/api/webhooks/628273795983081500/PwyoFg5wafFEpeecPO9RlnDyXpJD0pYJLUOIZhMpx_wC4GJaQexOlh48ogzlsI8YszfP'
   # if (carts == 1):

    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title=title, description=Link, color=242424)
    if(imageUrl != 'no image available'):
        embed.set_thumbnail(url=imageUrl)
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='type:', value=type)
    for cart in cartList:
        cartLink = cart['cartLink']
        embed.add_embed_field(name=cart['size'], value=(
            '[link]' + '(' + cart['cartLink']+')'))
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_unfilteded(cartList, imageUrl, Link, title, price, type='newly added'):
    sleep(0.3)

    webhook_url = 'https://discordapp.com/api/webhooks/656672291463233587/To5Zc09urpQEni2byUOoJK7OvNWkBjO3vIuWTqCEdXzNhuIQVJTFsddkHQ9Nw1CRpYka'
   # if (carts == 1):

    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title=title, description=Link, color=242424)
    if(imageUrl != 'no image available'):
        embed.set_thumbnail(url=imageUrl)
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='type:', value=type)
    for cart in cartList:
        cartLink = cart['cartLink']
        embed.add_embed_field(name=cart['size'], value=(
            '[link]' + '(' + cart['cartLink']+')'))
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_snkrs(image_url, link, title, price, active, style_code, exclusiveAccess, availability, method="N/A", date="N/A"):

    webhook_url = 'https://discordapp.com/api/webhooks/695019469688275014/ZmmQYPAstfR-g9sumR4wUjCfzfKH0zqhcf4B3ryxC_KNyCwWezvTlpAKLyjhTNXK35sh'

    webhook = DiscordWebhook(url=webhook_url)

    #general description
    embed = DiscordEmbed(title=title, url=link, description=link, color=15258703)
    #add image thumbnail
    embed.set_thumbnail(url=image_url)
    #other details
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='active:', value=active)
    embed.add_embed_field(name='style_code:', value=style_code)
    embed.add_embed_field(name='exclusiveAccess:', value=exclusiveAccess)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='method:', value=method)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_snkrs_non_product(image_url, link, title, date, description):
    webhook_url = 'https://discordapp.com/api/webhooks/695019469688275014/ZmmQYPAstfR-g9sumR4wUjCfzfKH0zqhcf4B3ryxC_KNyCwWezvTlpAKLyjhTNXK35sh'

    webhook = DiscordWebhook(url=webhook_url)

    # general description
    embed = DiscordEmbed(title=title, url=link, description=description, color=15258703)
    # add image thumbnail
    embed.set_thumbnail(url=image_url)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_nike(image_url, link, title, price, active, style_code, availability, date):

    webhook_url = 'https://discordapp.com/api/webhooks/695019469688275014/ZmmQYPAstfR-g9sumR4wUjCfzfKH0zqhcf4B3ryxC_KNyCwWezvTlpAKLyjhTNXK35sh'

    webhook = DiscordWebhook(url=webhook_url)

    #general description
    embed = DiscordEmbed(title=title, url=link, description=link, color=16711680)
    #add image thumbnail
    embed.set_thumbnail(url=image_url)
    #other details
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='active:', value=active)
    embed.add_embed_field(name='style_code:', value=style_code)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_bestbuy(name, link,type, availability):
    webhook_url = "https://discordapp.com/api/webhooks/695488518964772864/pfn_IZ5OlAi2-kPdBT5tW_QLSyCNmA7p6A1nob12HrLNmNI8VhCkhsF-0IDeSxJiGoY-"

    webhook = DiscordWebhook(url=webhook_url)

    # general description
    embed = DiscordEmbed(title=name, url=link, color=16711680)
    #embed.add_embed_field(type="type", value=type)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='type:', value=type)

    # execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_nike_cn(image_url, link, title, price, active, style_code, availability, date):

    webhook_url = 'https://discordapp.com/api/webhooks/697279046693945374/HCXccyiePRmx1qIW8Y5Xw4I79h5OewrF9EOnRzqBiTLrEfanPnHWPa8xdCEOCGAZoSuG'

    webhook = DiscordWebhook(url=webhook_url)

    #general description
    embed = DiscordEmbed(title=title, url=link, description=link, color=16711680)
    #add image thumbnail
    embed.set_thumbnail(url=image_url)
    #other details
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='active:', value=active)
    embed.add_embed_field(name='style_code:', value=style_code)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_snkrs_cn(image_url, link, title, price, active, style_code, exclusiveAccess, availability, method="N/A", date="N/A"):

    webhook_url = 'https://discordapp.com/api/webhooks/697279908103192597/1gaavvIFfX6YGeoEhn95lCVQshRCN87MPKxWT_vpHQznVOU1Rkmo1pvQeaGao7PdQodi'

    webhook = DiscordWebhook(url=webhook_url)

    #general description
    embed = DiscordEmbed(title=title, url=link, description=link, color=15258703)
    #add image thumbnail
    embed.set_thumbnail(url=image_url)
    #other details
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='active:', value=active)
    embed.add_embed_field(name='style_code:', value=style_code)
    embed.add_embed_field(name='exclusiveAccess:', value=exclusiveAccess)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='method:', value=method)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_snkrs_non_product_cn(image_url, link, title, date, description):
    webhook_url = 'https://discordapp.com/api/webhooks/697279908103192597/1gaavvIFfX6YGeoEhn95lCVQshRCN87MPKxWT_vpHQznVOU1Rkmo1pvQeaGao7PdQodi'

    webhook = DiscordWebhook(url=webhook_url)

    # general description
    embed = DiscordEmbed(title=title, url=link, description=description, color=15258703)
    # add image thumbnail
    embed.set_thumbnail(url=image_url)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_snkrs_us(image_url, link, title, price, active, style_code, exclusiveAccess, availability, method="N/A", date="N/A"):

    webhook_url = 'https://discordapp.com/api/webhooks/557006734154268692/aSZ4MeDuNfuh_iDMhuRfQ1ys7Z9BFAee1F4AX994FiJPojMwTYffRAYC_i266H52xp5i'

    webhook = DiscordWebhook(url=webhook_url)

    #general description
    embed = DiscordEmbed(title=title, url=link, description=link, color=15258703)
    #add image thumbnail
    embed.set_thumbnail(url=image_url)
    #other details
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='active:', value=active)
    embed.add_embed_field(name='style_code:', value=style_code)
    embed.add_embed_field(name='exclusiveAccess:', value=exclusiveAccess)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='method:', value=method)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_snkrs_non_product_us(image_url, link, title, date, description):
    webhook_url = 'https://discordapp.com/api/webhooks/557006734154268692/aSZ4MeDuNfuh_iDMhuRfQ1ys7Z9BFAee1F4AX994FiJPojMwTYffRAYC_i266H52xp5i'

    webhook = DiscordWebhook(url=webhook_url)

    # general description
    embed = DiscordEmbed(title=title, url=link, description=description, color=15258703)
    # add image thumbnail
    embed.set_thumbnail(url=image_url)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def notifyDisc_nike_us(image_url, link, title, price, active, style_code, availability, date):

    webhook_url = 'https://discordapp.com/api/webhooks/558108819507380245/aCIg7eSAN4sn4U3F4kAjyORxJahqG-_8hRWYP05f8K2ZEvyPQiUP9kISBU8OYksl5seJ'

    webhook = DiscordWebhook(url=webhook_url)

    #general description
    embed = DiscordEmbed(title=title, url=link, description=link, color=16711680)
    #add image thumbnail
    embed.set_thumbnail(url=image_url)
    #other details
    embed.add_embed_field(name='price:', value=price)
    embed.add_embed_field(name='active:', value=active)
    embed.add_embed_field(name='style_code:', value=style_code)
    embed.add_embed_field(name='availability:', value=availability)
    embed.add_embed_field(name='date:', value=date)
    #execution
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()