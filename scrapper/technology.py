'''
https://techcrunch.com/
https://thenextweb.com/
https://www.wired.com/

'''

import requests
from bs4 import BeautifulSoup

url = requests.get('https://techcrunch.com/')
url2 = requests.get('https://thenextweb.com/')
url3 = requests.get('https://www.wired.com/')