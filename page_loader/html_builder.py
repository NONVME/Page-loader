import os
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.url_formatter import to_filename
from page_loader.url_formatter import to_dirname


TAG_ATTRS = {
    'link': 'href',
    'img': 'src',
    'script': 'src',
}


def get_modified_page(url: str, page: str) -> tuple[str, list[str]]:
    original_links = []
    soup = BeautifulSoup(page, 'html.parser')
    assets_dir_path = to_dirname('', url, '_files/')

    for tag, attribute in TAG_ATTRS.items():
        for link in [node.get(attribute) for node in soup.find_all(name=tag)]:
            if (urlparse(link).netloc == urlparse(url).netloc
                    or urlparse(link).netloc == ''):

                original_links.append(link)
                path = os.path.join(assets_dir_path, to_filename(link, url))
                original_tag = soup.find(name=tag, **{attribute: link})
                original_tag[attribute] = path

    return soup.prettify(formatter="html5"), original_links
