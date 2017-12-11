import requests
from bs4 import BeautifulSoup

def ping_url(a_url):
    '''
    :param a_url: 
    :return: 
    '''

    url = requests.get(a_url)
    source = BeautifulSoup(url.text, 'html.parser')
    return source

