#GOAL: Clean up JSON output – add count of "innovation" words for each website, create cleaner, structured data

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

#Use "String slices" and .title() method to entract name of company after 'http://www.'

urls = ['https://www.aboutamazon.com/our-company', 'https://www.amerisourcebergen.com/about-who-we-are', 
       'https://www.unitedhealthgroup.com/about']
data = {}

for url in urls:
    
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    innovation_instances = soup.find_all(string=re.compile("inno*"))
    
    # add count of innovation words to dictionary and print as JSON/CSV element under 
    
    data[url] = innovation_instances
    
    #Convert innovation_instances to string and count instances
    
    def listToString():  
        ii_string = " " 

        # return string   
        return (ii_string.join(innovation_instances)) 

    string = listToString()
    sub = 'inno'
    
    inno_string = (string.count(sub))
    
    print (inno_string)
    
    innovation_instances.append(inno_string)
    
    
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
    
  
print(data)