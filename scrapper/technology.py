'''
https://techcrunch.com/
https://thenextweb.com/

'''

from .basescrapper import ping_url

def TechCrunchScrapper():
    one_post = []
    source = ping_url('https://techcrunch.com/')
    post_feed = source.find('div', id="container")
    posts = post_feed.find_all('div', id="content")
    for post in posts:
        title = post.find('div', class_='item-details')
        title = title.h3.text
        excerpt = post.find('div', class_='item-details')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
    return one_post

def TheNextWebScrapper():
    one_post = []
    source = ping_url('https://thenextweb.com/')
    post_feed = source.find('div', id="main-content")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
    return one_post