from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen

# This script will return full sentences that contain inno*

url = "https://www.amerisourcebergen.com/about-who-we-are"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')


innovation_instances = soup.find_all(string=re.compile("innovations|innovation|innovator|innovators|innovate|innovates|innovative"))

# ALTERNATIVE with regex: 
# innovation_instances = soup.find_all(string=re.compile("inno*"))

print(innovation_instances)
