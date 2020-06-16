from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import csv

url = "https://www.amerisourcebergen.com/about-who-we-are"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')


innovation_instances = soup.find_all(string=re.compile("inno*"))
# print(innovation_instances)

def createCSV():
    with open("innovation_sentences.csv", mode="w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Amerisourcebergen"])
        csvwriter.writerow([innovation_instances])
        
createCSV()

# ----------------export as json----------------


from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import json

url = "https://www.amerisourcebergen.com/about-who-we-are"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')


innovation_instances = soup.find_all(string=re.compile("inno*"))
# print(innovation_instances)

data = {'AmeriSource':[{'all_instances': innovation_instances}]}

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)