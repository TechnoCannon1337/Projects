import os
import os.path
from lxml import html
from lxml import *
from bs4 import *
import requests
import csv

broth = requests.get('URLtoScrape')
chicken = broth.content
soup = BeautifulSoup(chicken, 'html.parser')
for a in soup.findAll('a', href=True):
    a.extract()

meal = soup.select('JSPathtoPrint')
for bite in meal:
    print(str(bite))
