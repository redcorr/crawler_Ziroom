import requests
import random


def get_page(url):
    url_list = (
        {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        {'user-agent': "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        {'user-agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
        {'user-agent': "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"},
        {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    )
    user_agent = random.choice(url_list)
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        return response.text
