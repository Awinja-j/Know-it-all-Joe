'''
https://www.hollywoodreporter.com/
http://www.tmz.com/
https://www.popsugar.com/
'''
import requests
from bs4 import BeautifulSoup

class Urls(self):
    def ping_url(self, real_url):
        url = requests.get(real_url)
        source = BeautifulSoup(url.text, 'html.parser')
        return source

    def url1(self):
        '''scrapper for hollywood reporter'''
        source = self.ping_url('https://www.hollywoodreporter.com/')
        post_feed = source.find('div', class_="homepage-section")
        posts = post_feed.find_all('article', class_="homepage-item")
        meta = posts.find('div', text='movies', class_='homepage-item__meta')
        title = posts.find('h1', class_='homepage-item__title')
        excerpt = posts.find('p', class_='homepage-item__deck')
        excerpt = excerpt.text
        return {
            "title": title,
            "meta": meta,
            "excerpt": excerpt
        }

    def url2(self):
        '''scrapper for tmz'''
        source = self.ping_url('http://www.tmz.com/')
        post_feed = source.find('div', class_="post-feed")
        title = title
        excerpt = excerpt
        author = author
        return {
            "title": title,
            "excerpt": excerpt,
            "author": author
        }
    def url3(self):
        '''scrapper for pop sugar'''
        source = self.ping_url('https://www.popsugar.com/')
        post_feed = source.find('div', class_="post-feed")
        title = title
        excerpt = excerpt
        author = author
        return {
            "title": title,
            "excerpt": excerpt,
            "author": author
        }