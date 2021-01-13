import os
import re
from typing import Optional
from urllib.parse import urljoin, urlparse

URL_STRUCTURE = 'scheme://netloc/path;parameters?query#fragment'


def generate_name_page(forepart_path: str,
                       tail_path: str,
                       end_of_path: str) -> str:
    name = os.path.join(forepart_path, url_formatting(tail_path) + end_of_path)
    valid_name = truncate_name(name)
    return valid_name


def generate_name_link(dir_path: str,
                       domain: str,
                       link: str) -> str:
    domain = url_formatting(domain)
    link, ext = link_formatting(link)
    name = os.path.join(dir_path, domain + link + ext)
    valid_name = truncate_name(name)
    return valid_name


def url_formatting(url: str) -> str:
    valid_url = url_normalize(url)
    return re.sub(r'\W', '-', re.sub(r'^([a-zA-Z]+):\/\/', '', valid_url))


def link_formatting(link: str) -> tuple[str, str]:
    link, ext = os.path.splitext(link)
    return re.sub(r'\W', '-',  link), ext


def has_ext(url: str) -> bool:
    return bool(os.path.splitext(url)[1])


def is_correct_url(url: str) -> bool:
    parse_result = urlparse(url)
    return (all([parse_result.scheme, parse_result.netloc])
            and len(parse_result.netloc.split(".")) > 1)


def url_normalize(url: str) -> Optional[str]:
    url = str(url)
    segments = url.split('/')
    correct_segments = []
    for segment in segments:
        if segment != '':
            correct_segments.append(segment)
    first_segment = str(correct_segments[0])
    if first_segment.find('http') == -1:
        correct_segments = ['http:'] + correct_segments
    correct_segments[0] = correct_segments[0] + '/'
    url = '/'.join(correct_segments)
    if is_correct_url(url):
        return url
    else:
        raise ValueError(f'incorrect url introduced: {url}\n')


def truncate_name(name: str) -> str:
    return (name[:254] + '..') if len(name) > 255 else name


def get_domain(url: str) -> str:
    return urljoin(url, '/')
