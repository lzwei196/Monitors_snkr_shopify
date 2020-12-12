from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep

def send_webhook(title, link, url='https://discord.com/api/webhooks/783121758105370624/EE4RP3K_kNNskk_EfwsZZvg_QCh39-35m60qiUHcAcAeZ7plgWW_GtHP66rEJtbp9h4g'):
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=title, description=link, color=242424)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()