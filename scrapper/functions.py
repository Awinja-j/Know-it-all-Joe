import requests
from bs4 import BeautifulSoup

def ping_url(a_url):
    url = requests.get(a_url)
    source = BeautifulSoup(url.text, 'html.parser')
    return source


def loop_through(article):
    things = []
    return things = [get_post_details(article) for post in posts ];

def find_elements(element, identifier, classes):
    return element.find_all(identifier, class_=classes)

def find_text(element, identifier, classes):
    return element.find_all(identifier, class_=classes).text

def find_text_in_P(element, identifier, classes):
    return element.find_all(identifier, class_=classes).p.text

def find_text_in_link(element, identifier, classes):
    return element.find_all(identifier, class_=classes).a.text

def find_text_in_title(element, identifier, classes):
    return element.find_all(identifier, class_=classes).identifier.text