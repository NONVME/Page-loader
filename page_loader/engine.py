import logging
from urllib.parse import urljoin

from progress.bar import Bar

from page_loader.file import write
from page_loader.html_builder import process_html
from page_loader.http import get_data
from page_loader.url_formatter import to_dirname


logger = logging.getLogger(__name__)


def download(url: str, dir_path: str) -> str:
    abs_path = to_dirname(dir_path, url, '.html')
    assets_dirname = to_dirname(dir_path, url, '_files')

    page = get_data(url).text
    modified_page, original_links = process_html(url, page)
    write(modified_page, abs_path)
    logger.debug(f'page {url} was written in {abs_path}')

    bar = Bar(f'Loading: {url}', max=len(original_links))

    for link in original_links:
        resource_url = urljoin(url, link)
        assets_full_dirname = to_dirname(assets_dirname, url, link,
                                         is_link=True)
        assets = get_data(resource_url).content
        write(assets, assets_full_dirname, is_assets=True)
        logger.debug(f'content by {link} was written')
        bar.next()

    bar.finish()
    return abs_path
