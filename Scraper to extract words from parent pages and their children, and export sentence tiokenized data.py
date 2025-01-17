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
import nltk
nltk.download()



# Working URLs

urls = [

'http://Intel.com',
'http://Apple.com',
'http://Merck.com',
'http://corporate.ford.com',
'http://www.gm.com',
'http://Oracle.com',
'http://Celgene.com',
'http://QUALCOMM.com',
'http://www.lilly.com',
'http://AbbVie.com',
'http://Bristol-Myers.com',
'http://www.ge.com',
'http://Gilead.com',
'http://Amgen.com',
'http://Broadcom.com',
'http://www.boeing.com']

data = {}


# function that scrapes each URL 
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
    data[url] = string[0:1000], inno_string_count    
    
            

    
    with open("Qualcomm_truncate_test.json", 'w') as outfile:
            json.dump(data, outfile)

    
for url in urls:
      
#     time.sleep(3)
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    ssl._create_default_https_context = ssl._create_unverified_context
    html = urlopen(req, context=ssl.SSLContext()).read()     
              
    soup = BeautifulSoup(html, 'html.parser')
    

    
        # expand search
    links = [a['href'] for a in soup.find_all('a', href=True)] 

    base_url = url.split('/')
    base_url_joined = ''.join(base_url[0]) + '//' + base_url[2]



    for link in links: 
        if link[0:1] == '/' and link.endswith('.pdf' or '.svg') == False and "^privacy" not in link:
            scrape(base_url_joined + link)





