from apscheduler.schedulers.blocking import BlockingScheduler
import requests

channel_id = 'random'
apple_news_url = 'localhost'
syndication_new_url = 'localhost'

def loeader():
    r = requests.get(syndication_url)
    articles=r.json()

    for article in articles:
        upload_article_url = apple_news_url + '/channels/'+channel_id+ '/articles'
        r = requests.put(upload_article_url, json=article)


if __name__ == '__main__':
    sched = BlockingScheduler(timezone='EST')
    sched.add_job(loeader, 'interval', id='loeader',seconds=5)
    sched.start()
