from bs4 import BeautifulSoup
import requests
import json
import configparser


def load_articles(url,username,password):
    r = get_article_lists(url,username,password)
    links = get_article_links(r)
    articles = get_articles(links)
    return articles

def get_article_lists(url,username,password):
    headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    r=requests.get(url,auth=(username, password),headers=headers)
    return r

def get_article_links(r):
    soup = BeautifulSoup(r.text,"lxml")
    articles = []
    for link in soup.find_all('item'):
        articles.append(link.contents[6].strip()+'?renderer=json')
    return articles

def get_articles(links):
    articles=[]
    headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'upgrade-insecure-requests':'1',
    'pragma':'no-cache',
    'cache-control':'no-cache',
    'accept-language':'en-US,en;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br'
    }

    for link in links:
        try:
           r=requests.get(link,headers=headers)
           article = json.loads(r.text)
           articles.append(article)
        except:
            print(link)
    return articles
