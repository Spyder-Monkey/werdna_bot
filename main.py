import requests
from bs4 import BeautifulSoup
import discord
import os
from dotenv import load_dotenv


client = discord.Client




#URL = 'https://en.wikipedia.org/wiki/Suburb'
#page = requests.get(URL)

#soup = BeautifulSoup(page.content, 'html.parser')

#results = soup.find(id="bodyContent")
#print(results.prettify())

#section = results.find_all('div', class_='card-content')

#for job_element in job_elements:
#    title_element = job_element.find('h2', class_='title')
#    company_element = job_element.find('h3', class_='company')
#    location_element = job_element.find('p', class_='location')
#    print(title_element.text.strip())
#    print(company_element.text.strip())
#    print(location_element.text.strip())
#    print()