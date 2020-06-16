from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import json

# define two URLs for two different companies
url = "https://www.amerisourcebergen.com/about-who-we-are"
url2 = "https://www.aboutamazon.com/our-company"

html = urlopen(url)
html2 = urlopen(url2)

soup = BeautifulSoup(html, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')

innovation_instances_AmeriSource = soup.find_all(string=re.compile("inno*"))
innovation_instances_Amazon = soup2.find_all(string=re.compile("inno*"))

data = {'AmeriSource':[{'all_instances': innovation_instances_AmeriSource}]},{'Amazon':[{'all_instances': innovation_instances_Amazon}]}

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)