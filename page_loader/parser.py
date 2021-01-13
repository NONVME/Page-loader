from collections import deque
from typing import Union
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.formaters import link_formatting, url_formatting
from page_loader.formaters import generate_name_page

ORIGINAL_LINKS = deque()


def without_domain(href: str) -> Union[bool, str]:
    return href and not urlparse(href)[1] != ''


def parse(url: str, page: str, dir_path: str) -> str:
    soup = BeautifulSoup(page, 'html5lib')
    assets_dir_path = generate_name_page(forepart_path=dir_path,
                                         tail_path=url,
                                         end_of_path='_file/')

    for tag in soup.find_all(name='link', href=without_domain):
        ORIGINAL_LINKS.append(tag['href'])
        path, ext = link_formatting(tag['href'])
        tag['href'] = assets_dir_path + url_formatting(url) + path + ext

    for tag in soup.find_all(name=['img', 'script'], src=without_domain):
        ORIGINAL_LINKS.append(tag['src'])
        path, ext = link_formatting(tag['src'])
        tag['src'] = assets_dir_path + url_formatting(url) + path + ext

    return soup.prettify(formatter="html5")
