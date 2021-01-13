import os
from typing import Optional

import requests

from page_loader.constants import CHROME_DESKTOP
from page_loader.formaters import generate_name_link, generate_name_page
from page_loader.formaters import get_domain, has_ext, url_normalize
from page_loader.parser import ORIGINAL_LINKS, parse


def download(url: str, dir_path: str) -> str:
    url = url_normalize(url)
    full_path_page = generate_name_page(forepart_path=dir_path,
                                        tail_path=url,
                                        end_of_path='.html')
    parsed_page = parse(url, get_page(url), dir_path)
    write(parsed_page, full_path_page, dir_path)
    for link in ORIGINAL_LINKS:
        domain_link = url_normalize(get_domain(url) + link)
        if domain_link == url or domain_link == url + '/':
            break
        elif has_ext(link):
            assets_dir_path = generate_name_page(forepart_path=dir_path,
                                                 tail_path=url,
                                                 end_of_path='_file')
            assets_full_path = generate_name_link(dir_path=assets_dir_path,
                                                  domain=url,
                                                  link=link)
            write(get_page(domain_link), assets_full_path, assets_dir_path)
        else:
            download(domain_link, dir_path)
    return full_path_page


def get_page(url: str) -> Optional[str]:
    headers = {'user-agent': CHROME_DESKTOP}
    try:
        response = requests.get(url, headers=headers, timeout=1)
    except requests.exceptions.ReadTimeout:
        print('Reconnecting to servers, maximum latency 30 seconds\n')
        response = requests.get(url, headers=headers, timeout=30)
    else:
        if response.ok:
            return response.text
        else:
            raise ConnectionError(
                f'http response: {response.status_code}\nRequested page: {url}'
                if response.status_code == 404
                else f'http response: {response.status_code}\n')


def write(data: Optional[str], full_path: str, dir_path: str) -> None:
    if data:
        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(data)
        except FileNotFoundError:
            os.mkdir(dir_path)
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(data)
    else:
        raise ValueError(f'Requested page is: {data}\n')
