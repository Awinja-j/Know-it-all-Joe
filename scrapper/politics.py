'''
https://www.huffingtonpost.com/
https://www.washingtontimes.com/

'''
from .basescrapper import ping_url

def HuffingtonPostScrapper():
    one_post = []
    source = ping_url('https://www.huffingtonpost.com/')
    post_feed = source.find('div', id="main-content")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
        return one_post

def WashingtonTimesScrapper():
    one_post = []
    source = ping_url('https://www.washingtontimes.com/')
    post_feed = source.find('div', id="main-content")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
        return one_post