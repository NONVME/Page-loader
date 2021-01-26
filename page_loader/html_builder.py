import os
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.url_formatter import to_filename
from page_loader.url_formatter import to_dirname


def get_modified_page(url: str, page: str) -> tuple[str, list[str]]:

    def is_local_resource(link: str) -> bool:

        domains_are_eq = urlparse(link).netloc == urlparse(url).netloc
        status = bool(link) and urlparse(link).netloc == '' or domains_are_eq
        return status

    original_links = []
    soup = BeautifulSoup(page, 'html5lib')

    assets_dir_path = to_dirname('', url, '_file/')

    for tag in soup.find_all(name='link', href=is_local_resource):
        original_links.append(tag['href'])
        path = os.path.join(assets_dir_path,
                            to_filename(url) + to_filename(tag['href']))
        tag['href'] = path

    for tag in soup.find_all(name=['img', 'script'], src=is_local_resource):
        original_links.append(tag['src'])
        path = os.path.join(assets_dir_path,
                            to_filename(url) + to_filename(tag['src']))
        tag['src'] = path

    return soup.prettify(formatter="html5"), original_links
