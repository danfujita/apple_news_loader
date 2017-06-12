from apscheduler.schedulers.blocking import BlockingScheduler
import configparser
import requests


config = configparser.ConfigParser()
config.read('config.ini')

def loader():
    channel_id =config['URLS']['channel_id']
    apple_news_url = config['URLS']['apple_news_url']
    syndication_url = config['URLS']['syndication_url']

    r = requests.get(syndication_url)
    articles=r.json()

    for article in articles:
        upload_article_url = apple_news_url + '/channels/'+channel_id+ '/articles'
        r = requests.put(upload_article_url, json=article)


if __name__ == '__main__':
    sched = BlockingScheduler(timezone='EST')
    sched.add_job(loader, 'interval', id='loeader',minutes=int(config['INTERVAL']['minutes']))
    sched.start()
