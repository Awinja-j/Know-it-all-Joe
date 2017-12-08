'''
https://finance.yahoo.com/
https://www.msn.com/
http://money.cnn.com/
'''
import requests
from bs4 import BeautifulSoup

url = requests.get('https://finance.yahoo.com/')
url2 = requests.get('https://www.msn.com/')
url3 = requests.get('http://money.cnn.com/')