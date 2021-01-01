import re
import os

import requests

from page_loader.constants import CHROME_DESKTOP


def download(url, output):
    file_name = generate_name(url, output)
    save_page(get_page(url).text, file_name)
    return file_name


def generate_name(url, output):
    url = re.sub(r'\W', '-', re.sub(r'^([a-zA-Z]+):\/\/', '', url))
    return os.path.join(output, url + '.html')


def get_page(url):
    headers = {'user-agent': CHROME_DESKTOP}
    response = requests.get(url, headers=headers, timeout=1)
    if response.ok:
        return response
    else:
        return None


def save_page(page, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(page)
