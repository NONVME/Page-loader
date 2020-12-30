import re
import os

import requests


def download(url, output):
    file_name = generate_name(url, output)
    save_page(get_page(url).text, file_name)
    return file_name


def generate_name(url, output):
    url = re.sub(r'\W', '-', re.sub(r'^([a-zA-Z]+):\/\/', '', url))
    return os.path.join(output, url + '.html')


def get_page(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers, timeout=1)
    return r


def save_page(page, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(page)
