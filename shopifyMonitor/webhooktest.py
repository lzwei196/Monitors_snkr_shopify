from discord_webhook import DiscordWebhook, DiscordEmbed


webhook_url = 'https://discordapp.com/api/webhooks/560354284429115393/TcQ_Gog4v15zy6yiL3BleLoDvSeFYDG7-km4W1y6Q2vSQSnWeUEi16oJVhaW_LiAeY6w'
    #    # if (carts == 1):
webhook = DiscordWebhook(url=webhook_url)
embeds = DiscordEmbed(title='go', url='https://www.google.com', color=242424)
embeds.add_embed_field(name='8', value=('[link]' + '(' + 'https://www.google.com'+')'))
print(embeds)
webhook.add_embed(embeds)

webhook.execute()



