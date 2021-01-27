import os
import re
import tempfile
from typing import Union
from urllib.parse import urlparse


def to_dirname(dirname: str, url: str,
               ext: str, *, is_link: bool = False) -> str:
    if is_link:
        name = os.path.join(dirname, to_filename(ext, url))
    else:
        filename = to_filename(url, urlparse(url).netloc)
        name = os.path.join(dirname, filename + ext)
    return truncate_name(name)


def to_filename(url: str, domain: str) -> str:
    re_path = re.compile(r'[^a-zA-Z0-9]')
    re_scheme = re.compile(r'^https?:\/\/')
    url, ext = os.path.splitext(url)
    if re_scheme.match(url):
        filename = re_path.sub('-', re_scheme.sub('', url)) + ext
    else:
        ext = '.html' if ext == '' else ext
        filename = (re_path.sub('-', urlparse(domain).netloc) +
                    re_path.sub('-', url) + ext)
    return filename


def has_ext(url: str) -> bool:
    return bool(os.path.splitext(url)[1])


def truncate_name(path_file: Union[str, bytes]) -> str:
    path_file = os.fsdecode(path_file)
    path, filename = os.path.split(path_file)
    name_max = os.pathconf('/', 'PC_NAME_MAX') - 1
    if len(filename) >= name_max:
        filename, ext = os.path.splitext(filename)
        file_uniqueness = next(tempfile._get_candidate_names())
        name_len = name_max - len(filename) - len(file_uniqueness) - len(ext)
        filename = filename[:name_len] + file_uniqueness + ext
        path_file = os.path.join(path, filename)
        if os.path.exists(path_file):
            truncate_name(path_file)
    return path_file


def get_domain(url: str) -> str:
    domain = urlparse(url).netloc
    return domain
