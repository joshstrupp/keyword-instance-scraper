#NOTE: there are simple JSON to CSV converters: https://json-csv.com

# ------------------------------------------

from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import json


urls = ['https://www.aboutamazon.com/our-company', 'https://www.amerisourcebergen.com/about-who-we-are']
data = {}

for url in urls:
    
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    innovation_instances = soup.find_all(string=re.compile("inno*"))
    
    # add count of innovation words to dictionary and print as JSON/CSV element under 
    
    data[url] = innovation_instances
    
    #Convert innovation_instances to string and count instances
    
    def listToString(s):  
        ii_string = " " 

        # return string   
        return (ii_string.join(innovation_instances)) 

    string = listToString(s)
    sub = 'inno'
    
    print (string.count(sub))
    
    
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
    
  
print(data)


