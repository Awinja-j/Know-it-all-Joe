'''
https://www.treehugger.com/
http://www.realclimate.org/
http://grist.org/
'''
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.treehugger.com/')
url2 = requests.get('http://www.realclimate.org/')
url3 = requests.get('http://grist.org/')