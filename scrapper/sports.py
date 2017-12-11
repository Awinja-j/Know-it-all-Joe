'''
http://www.espn.com/
https://sports.yahoo.com/

'''
from .basescrapper import ping_url

def ESPNScrapper():
    one_post = []
    source = ping_url('http://www.espn.com/')
    post_feed = source.find('div', id="main-content")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
        return one_post

def YahooSportsScrapper():
    one_post = []
    source = ping_url('https://sports.yahoo.com/')
    post_feed = source.find('div', id="main-content")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
        return one_post