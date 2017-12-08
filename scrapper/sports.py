'''
http://www.espn.com/
https://sports.yahoo.com/
http://www.goal.com/en-ke/

'''
import requests
from bs4 import BeautifulSoup

url = requests.get('http://www.espn.com/')
url2 = requests.get('https://sports.yahoo.com/')
url3 = requests.get('http://www.goal.com/en-ke/')