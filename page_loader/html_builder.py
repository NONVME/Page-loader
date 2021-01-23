import os
from typing import Union
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.url_formatter import to_filename
from page_loader.url_formatter import to_dirname


def without_domain(url: str) -> Union[bool, str]:
    return url and not urlparse(url).netloc != ''


def get_modified_page(url: str, page: str,
                      dir_path: str) -> tuple[str, list[str]]:
    original_links = []
    soup = BeautifulSoup(page, 'html5lib')

    assets_dir_path = to_dirname(dir_path, url, '_file/')

    for tag in soup.find_all(name='link', href=without_domain):
        original_links.append(tag['href'])
        path = os.path.join(assets_dir_path,
                            to_filename(url) + to_filename(tag['href']))
        tag['href'] = path

    for tag in soup.find_all(name=['img', 'script'], src=without_domain):
        original_links.append(tag['src'])
        path = os.path.join(assets_dir_path,
                            to_filename(url) + to_filename(tag['src']))
        tag['src'] = path

    return soup.prettify(formatter="html5"), original_links
