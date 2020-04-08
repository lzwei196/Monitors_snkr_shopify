from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep


def notifyDisc(cartList, imageUrl, Link, title, price, type='newly added'):
    sleep(0.3)

    webhook_url = ''
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

    webhook_url = ''
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

    webhook_url = ''
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

    webhook_url = ''

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
    webhook_url = ''

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

    webhook_url = ''

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
    webhook_url = ""

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

    webhook_url = ''

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

    webhook_url = ''

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
    webhook_url = ''

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
