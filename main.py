from apscheduler.schedulers.blocking import BlockingScheduler
import requests

channel_id = 'random'
apple_news_url = 'localhost'

def loeader():
    articles = []
    for article in articles:
        r = requests.put(apple_news_url + '/channels/'+{channel_id}+ '/articles', json=article)


if __name__ == '__main__':
    sched = BlockingScheduler(timezone='EST')
    sched.add_job(loeader, 'interval', id='loeader',seconds=5)
    sched.start()
