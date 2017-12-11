'''
https://www.treehugger.com/
http://www.realclimate.org/
'''
from .basescrapper import ping_url

def TreeHuggerScrapper():
    one_post = []
    source = ping_url('https://www.treehugger.com/')
    post_feed = source.find('div', id="container")
    posts = post_feed.find_all('div', id="content")
    for post in posts:
        title = post.find('div', class_='item-details')
        title = title.h3.text
        excerpt = post.find('div', class_='item-details')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
    print(one_post)
    return one_post

def GristScrapper():
    one_post = []
    source = ping_url('http://grist.org/')
    post_feed = source.find('div', class_="off-canvas-wrap")
    posts = post_feed.find_all('article', 'news')
    for post in posts:
        title = post.findAll('span', class_=['hf1', 'hf2'])
        excerpt = post.find('div', class_='article-content')
        excerpt = excerpt.p.text
        one_post.append({title, excerpt})
    print(one_post)
    return one_post