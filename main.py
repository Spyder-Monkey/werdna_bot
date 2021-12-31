from nltk.translate.phrase_based import extract
import requests
from bs4 import BeautifulSoup
import discord
import os
from dotenv import load_dotenv
import json
import re
from phrase_processing import *


# Simple Sentences: A simple sentence is an independent clause with no conjunction or dependent clause

# Compound Sentences: A compound sentence is two independent clauses joined by a conjunction (e.g., and, but, or, for, nor, yet, so).

# Complex Sentences: Contains one independent clause and at least one dependent clause. The clauses in a complex sentence
#   are combined with conjuctions and subordinators, terms that help the dependent clauses relate to the independent cluase
#   Suboridinators can refer to the subject (who, which), the sequence/time (since, while), or the casual elements (because, if) of
#   the independent clause.

# Compound-complex Sentences: Contains multiple independent clauses and at least one dependent clause.
#   These sentences will contain both conjunctions and subordinators.


# Independent Clause: Can stand alone as a sentence. Contains a subject and a verb and is a complete idea
#   e.g. "I like spaghetti." subject="I", verb="like", object="spaghetti"
#        "He reads many books." subject="He", verb="reads", object="many books"

# Dependent Clause: Not a complete sentence. It must be attached to an independent clause to become complete
#   This is also known asa a subordinate clause.
#   e.g. "Although I like spaghetti,..."
#        "Because he reads many books,..."


# A sentence follows (Subject + Verb + Object) word order

# Subject: A person, animal, place, thing, or concept that does an action. Determine the subject in a
#   sentence by asking the question "Who or what"



# Triggers: grass, suburbs, ohio state, russian hats, 


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
            # get topic of message and webscrape wikipedia    
            print('TOGGLE ARGUE')
        if str(message.channel) == 'bot-training-grounds':
            if str(message.author) == 'Spyder#5038' or str(message.author) == 'solsticesam#1337' or str(message.author) == 'jkc_boi#4751':
                contents = message.content

                ne = extract_ne(contents)
                #await message.reply(f"Named Entities: {extract_ne(contents)}")
                named_entities(contents)

                #if contents.find('grass') > -1:
                #await message.reply('%s you too buddy' % message.content)
                print("%s: %s" % (message.author, message.content))
            


# Load secrets file and get token
load_dotenv('secrets.env')
API_TOKEN = os.getenv('DISCORD_TOKEN')

client = WerdnaBot()
client.run(API_TOKEN)