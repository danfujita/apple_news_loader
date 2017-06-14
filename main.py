from apscheduler.schedulers.blocking import BlockingScheduler
import configparser
import requests
from rss.load_articles import load_articles
from converter import convert

config = configparser.ConfigParser()
config.read('config.ini')

def loader():
    channel_id =config['URLS']['channel_id']
    apple_news_url = config['URLS']['apple_news_url']
    syndication_url = config['URLS']['syndication_url']
    articles = load_articles(config['URLS']['syndication_url'],config['AUTH']['username'],config['AUTH']['password'])
    for article in articles:
        apple_news_article = convert(article)
        '''
        upload_article_url = apple_news_url + '/channels/'+channel_id+ '/articles'
        r = requests.put(upload_article_url, json=article)
        '''


if __name__ == '__main__':
    sched = BlockingScheduler(timezone='EST')
    sched.add_job(loader, 'interval', id='loeader',minutes=int(config['INTERVAL']['minutes']))
    sched.start()
