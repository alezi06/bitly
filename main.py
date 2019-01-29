import os
import requests
import argparse
from urllib.parse import urlparse

from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
AUTH_TOKEN = 'Bearer {}'.format(ACCESS_TOKEN)
HEADERS = {'Authorization': AUTH_TOKEN}
URL = 'https://api-ssl.bitly.com/v4/bitlinks'


def get_url_without_scheme(url):
    url_chunks = urlparse(url)
    return '{}{}'.format(url_chunks.netloc, url_chunks.path)


def get_short_link(long_url):
    body = {"long_url": long_url}
    response = requests.post(URL, headers=HEADERS, json=body)
    if response.ok:
        return response.json()['link']


def get_click_count(short_link):
    url = '{}/{}/clicks/summary'.format(URL,
                                        get_url_without_scheme(short_link))
    response = requests.get(url, headers=HEADERS)
    if response.ok:
        return response.json()['total_clicks']


def is_bitlink(link):
    url = '{}/{}'.format(URL, get_url_without_scheme(link))
    response = requests.get(url, headers=HEADERS)
    return response.ok


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Link')
    args = parser.parse_args()
    link = args.link

    if is_bitlink(link):
        click_count = get_click_count(link)
        if click_count is None:
            print('Invalid link')
        else:
            print(click_count)
    else:
        short_link = get_short_link(link)
        if short_link is None:
            print('Invalid link')
        else:
            print(short_link)
