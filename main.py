import requests
from bs4 import BeautifulSoup
import discord
import os
from dotenv import load_dotenv


# Trigger words
#   Grass, suburbs, ohio state, 

class WerdnaBot(discord.Client):
    def __init__(self):
        super().__init__()

    # Overridden method
    # Event method for when message is sent into chat
    # Message parameter holds all information about message
    async def on_message(self, message):
        # Safety so bot doesn't inifinitely respond to himself
        if message.author == client.user: return
        if str(message.author) == 'ArborO#7508':
            # get topic of message and webscrapte wikipedia    
            print('TOGGLE ARGUE')
        if str(message.author) == 'Spyder#5038':
            contents = message.content
            #if contents.find('grass') > -1:
            await message.reply('%s you too buddy' % message.content)
            print("SPYDER: ", message.content)



# Load secrets file and get token
load_dotenv('secrets.env')
API_TOKEN = os.getenv('DISCORD_TOKEN')

client = WerdnaBot()
client.run(API_TOKEN)