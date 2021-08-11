"""
main.py
Author: Diego Lopez
Date: 08-11-2021
This file runs the function scrape in scraper.py and communicates to the discord API to have it ping 
whenever the product is in stock. I use discord here but this could easily be any other communications platform.
"""

import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from scraper import scrape

load_dotenv()
TOKEN             = os.getenv('DISCORD_TOKEN')
GUILD             = os.getenv('DISCORD_SERVER')
CHANNEL_ID        = int(os.getenv("CHANNEL_ID"))
intents           = discord.Intents.default()
intents.members   = True
intents.typing    = False
intents.presences = False
client            = discord.Client(intents=intents)
url               = "https://barlowesherbalelixirs.com/fadogia-agrestis-extract"


@client.event 
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    scrape_to_discord.start(url)

@tasks.loop(minutes=0.5)
async def scrape_to_discord(url):
    in_stock = scrape(url)
    channel = client.get_channel(CHANNEL_ID)
    if in_stock:
        await channel.send(
        f""" {url} 
    IN STOCK!
        """)

client.run(TOKEN)
