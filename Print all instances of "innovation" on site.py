from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re

r = urllib.request.urlopen('https://www.amerisourcebergen.com/').read()
soup = BeautifulSoup(r, "lxml")

print(soup.get_text("innovation"))