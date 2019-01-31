import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


URL = 'https://api-ssl.bitly.com/v4/bitlinks'


def get_headers(access_token):
    return {
        'Authorization': 'Bearer {}'.format(access_token)
    }


def get_url_without_scheme(url):
    url_chunks = urlparse(url)
    return '{}{}'.format(url_chunks.netloc, url_chunks.path)


def get_short_link(long_url, access_token):
    headers = get_headers(access_token)
    body = {"long_url": long_url}
    response = requests.post(URL, headers=headers, json=body)
    if response.ok:
        return response.json()['link']


def get_click_count(short_link, access_token):
    url = '{}/{}/clicks/summary'.format(URL,
                                        get_url_without_scheme(short_link))
    headers = get_headers(access_token)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()['total_clicks']


def is_bitlink(link, access_token):
    url = '{}/{}'.format(URL, get_url_without_scheme(link))
    headers = get_headers(access_token)
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('ACCESS_TOKEN')

    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Link')
    args = parser.parse_args()
    link = args.link

    if is_bitlink(link, token):
        click_count = get_click_count(link, token)
        if click_count is None:
            print('Invalid link')
        else:
            print(click_count)
    else:
        short_link = get_short_link(link, token)
        if short_link is None:
            print('Invalid link')
        else:
            print(short_link)
