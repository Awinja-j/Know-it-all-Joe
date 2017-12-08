'''
https://www.huffingtonpost.com/
https://www.washingtontimes.com/
http://thehill.com/

'''
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.huffingtonpost.com/')
url2 = requests.get('https://www.washingtontimes.com/')
url3 = requests.get('http://thehill.com/')