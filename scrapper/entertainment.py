'''
https://www.hollywoodreporter.com/
http://www.tmz.com/
'''
from .basescrapper import ping_url

def TMZ_Scrapper():
    one_post = []
    source = ping_url('http://www.tmz.com/')
    post_feed = source.find('div', id="main-content")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
    return one_post

def HollywoodReporter_Scrapper():
    one_post = []
    source = ping_url('https://www.hollywoodreporter.com/')
    post_feed = source.find('div', 'homepage-section')
    posts = post_feed.find_all('article', 'homepage-item')
    for post in posts:
        title = post.find('h1', class_='homepage-item__title')
        excerpt = post.find('p', class_='homepage-item__deck')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
    return one_post
