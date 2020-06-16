from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import Request, urlopen
import json
import csv
import time
from datetime import datetime 
import os, ssl

urls = [
#         DOESNT RUN!? 'http://www.aboutamazon.com/our-company/']
        'http://www.intel.com/content/www/us/en/company-overview/company-overview.html',
        'http://www.microsoft.com/en-us/about/',
        'http://www.corporate.ford.com/company.html',
        'http://www.boeing.com/company/general-info',
        'http://www.alliancedata.com/about-us/default.aspx',
        'https://www.polarityte.com/about/overview/',
        'http://www.arconic.com/what-we-do/',
        'http://www.fico.com/en/about-us/',
        'http://www.epizyme.com/about-us/overview-history/']

data = {}


# function that scrapes each URL, 
def scrape(url):
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ssl._create_default_https_context = ssl._create_unverified_context
    
    html = urlopen(req, context=ssl.SSLContext()).read()
    soup = BeautifulSoup(html, 'html.parser')

    innovation_instances = soup.find_all(string=re.compile("inno+"))

    def listToString():  
        ii_string = " " 

        # return string   
        return (ii_string.join(innovation_instances)) 

    string = listToString()
    sub = 'inno'
    
    inno_string_count = (string.count(sub))
    
    data[url] = innovation_instances, inno_string_count
    
            
    print(data)
    
#     with open("data.txt", 'a') as outfile:
#             json.dump(data, outfile)

    
for url in urls:
    

#     time.sleep(5)
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ssl._create_default_https_context = ssl._create_unverified_context
    
    html = urlopen(req, context=ssl.SSLContext()).read()
    soup = BeautifulSoup(html, 'html.parser')
    
#     try:
        
#     except requests.HTTPError, e:
#     if e.response.status_code in [404, 410, 400]:
#         continue

    
    # expand search
    links = [a['href'] for a in soup.find_all('a', href=True)] 
    
    base_url = url.split('/')
    base_url_joined = ''.join(base_url[0]) + '//' + base_url[2]
    
    
    
    for link in links: 
        if link[0:1] == '/' and link.endswith('.pdf') == False:
            scrape(base_url_joined + link)

