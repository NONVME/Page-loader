import logging

from progress.bar import Bar

from page_loader.file import write
from page_loader.html_builder import get_modified_page
from page_loader.http import get_data
from page_loader.url_formatter import to_dirname
from page_loader.url_formatter import get_domain, url_normalize


logger = logging.getLogger(__name__)


def download(url: str, dir_path: str) -> str:
    url = url_normalize(url)
    full_dirname = to_dirname(dir_path, url, '.html')
    assets_dirname = to_dirname(dir_path, url, '_file')

    page = get_data(url).text
    modified_page, original_links = get_modified_page(url, page, dir_path)
    write(modified_page, full_dirname)
    logger.debug(f'page {url} was written in {full_dirname}')

    bar = Bar(f'Loading: {url}', max=len(original_links))

    for link in original_links:
        domain_link = url_normalize(get_domain(url) + link)
        assets_full_dirname = to_dirname(assets_dirname, url, link,
                                         is_link=True)
        assets = get_data(domain_link).content
        write(assets, assets_full_dirname)
        logger.debug(f'content by {link} was written')
        bar.next()

    bar.finish()
    return f'Page saved in {full_dirname}'
