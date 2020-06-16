from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import Request, urlopen
import json
# import csv
import time
from datetime import datetime 
import os, ssl
# import nltk

# Working URLs

urls = [

'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=1',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=2',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=2',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=3',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=4',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=5',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=6',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=7',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=8',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=9',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=10',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=11',
'https://www.uschamberfoundation.org/aid-event/coronavirus-covid-19?page=12']

data = {}


# function that scrapes each URL 
for url in urls:
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ssl._create_default_https_context = ssl._create_unverified_context
    
    html = urlopen(req, context=ssl.SSLContext()).read()
    soup = BeautifulSoup(html, 'html.parser')
        
#     covid_instances = soup.find_all(string=re.compile("Boeing+"))
    
#     company = soup.findAll(href=re.compile("/aid-event/coronavirus-covid-19/"))
#     donation_description = soup.find("div", {"class": "field field-name-field-pproject-description field-type-text-with-summary field-label-hidden"})
    
    
    
    company = [i.text for i in soup.findAll(href=re.compile("/aid-event/coronavirus-covid-19/"))]
    donation_description = [i.text for i in soup.findAll("div", {"class": "field field-name-field-pproject-description field-type-text-with-summary field-label-hidden"})]
    
    
    
    
    data[url] = [company, "**********__________________________*******", donation_description]
#     print(data)        

    
    with open("covid-commerce-data-april-1.json", 'w') as outfile:
            json.dump(data, outfile)



