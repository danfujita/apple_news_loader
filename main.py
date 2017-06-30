# from apscheduler.schedulers.blocking import BlockingScheduler
# import requests
import configparser
from rss.load_articles import load_articles, get_articles
from converter import convert
import json
import os
import sys

config = configparser.ConfigParser()
config.read('config.ini')


def load_from_feed():
    '''
    channel_id =config['URLS']['channel_id']
    apple_news_url = config['URLS']['apple_news_url']
    syndication_url = config['URLS']['syndication_url']
    '''
    articles = load_articles(
        config['URLS']['syndication_url'],
        config['AUTH']['username'],
        config['AUTH']['password']
    )

    for article in articles:
        convert_and_save(article)


def load_urls(urls):
    articles = get_articles(urls)
    for article in articles:
        convert_and_save(article)


def convert_and_save(article_json):
    apple_news_article = convert(article_json)
    article_id = apple_news_article['identifier']
    dir_path = 'articles/article/{0}'.format(article_id)
    article_path = '{0}/article.json'.format(dir_path)
    try:
        os.makedirs(dir_path, exist_ok=True)
        with open(article_path, 'w+') as outfile:
            json.dump(apple_news_article, outfile, indent=4)
    except:
        print('parse error')

    '''
    upload_article_url = apple_news_url + '/channels/'+channel_id+ '/articles'
    r = requests.put(upload_article_url, json=article)
    '''


if __name__ == '__main__':
    # convert specific urls passed in as cli arguments
    if len(sys.argv) > 1:
        urls = [arg for i, arg in enumerate(sys.argv) if i != 0]
        load_urls(urls)
    # otherwise pull from rss feed
    else:
        load_from_feed()
        '''
        sched = BlockingScheduler(timezone='EST')
        sched.add_job(
            loader,
            'interval',
            id='loeader',
            minutes=int(config['INTERVAL']['minutes'])
        )
        sched.start()
        '''
