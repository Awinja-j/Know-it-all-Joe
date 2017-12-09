'''
https://www.hollywoodreporter.com/
http://www.tmz.com/
https://www.popsugar.com/
'''

import requests
from bs4 import BeautifulSoup

def ping_url(a_url):
    url = requests.get(a_url)
    source = BeautifulSoup(url.text, 'html.parser')
    return source


def loop_through(posts, title_type, title_div, paragraph, paragraph_div):
    one_posts = []
    for post in posts:
        one_posts.append(get_elements(post, title_type, title_div, paragraph, paragraph_div))
        print("---post", post)
        print("---one post", one_posts)
        return one_posts

def find_elements(element, identifier, classes):
    return element.find_all(identifier, class_=classes)

def find_an_element(element, identifier, classes):
    return element.find(identifier, class_=classes)

def find_text(element, identifier, classes):
    return element.find(identifier, class_=classes)

def find_text_in_P(element, identifier, classes):
    return element.find(identifier, class_=classes)

def find_text_in_link(element, identifier, classes):
    return element.find(identifier, class_=classes).a.text

def find_text_in_title(element, identifier, classes):
    return element.find(identifier, class_=classes)


def get_elements(posts, title_type, title_div, paragraph, paragraph_div):
    title = find_text_in_title(posts, title_type, title_div)
    print("---title", title)
    excerpt = find_text_in_P(posts, paragraph, paragraph_div)
    print("----excerpt", excerpt)
    return {
        "title": title,
        "excerpt": excerpt
    }

def scrapper(url, home_div, homepage_section, article_name, article_div_name, title_type, title_div, paragraph, paragraph_div ):
    '''
     url: the url of the site you want to scrape
     home_div: this is the div where the post feed comes from, on the home page is just 'div'
     homepage_section: this is the name of the div class where the post feed comes from eg homepage-section
     article_name: is just 'article '
     article_div_name: the name of the div class that holds the articles eg homepage-item
     title_type: eg h1, h2, h3
     title_div: this is the div class of the title eg homepage-item__title
     paragraph: is just 'p'
     paragraph_div: this is the div class of the paragraph eg homepage-item__deck
     
    '''
    source = ping_url(url)
    post_feed = find_an_element(source, home_div, homepage_section)
    posts = find_elements(post_feed, article_name, article_div_name)
    print("----posts", posts)
    see = loop_through(posts, title_type, title_div, paragraph, paragraph_div)
    print("----see", see)
    return see




# scrapper('https://www.hollywoodreporter.com/', 'div', 'homepage-section', 'article', 'homepage-item', 'h1', 'homepage-item__title', 'p', 'homepage-item__deck')
scrapper('http://www.tmz.com/', 'div', 'page', 'article', 'news', 'h1', 'hf1', 'p', 'article-content')
# scrapper('https://www.popsugar.com/')