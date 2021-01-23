import os
import re
import tempfile
from typing import Union
from urllib.parse import urljoin


def to_dirname(dirname: str, url: str,
               ext: str, *, is_link: bool = False) -> str:
    filename = to_filename(url)
    name = os.path.join(dirname, filename + ext)
    if not is_link:
        return truncate_name(name)
    end_of_filename = to_filename(ext)
    name = os.path.join(dirname, filename + end_of_filename)
    return truncate_name(name)


def to_filename(url: str) -> str:
    valid_url = url_normalize(url)
    re_path = re.compile(r'[^a-zA-Z0-9]')
    re_scheme = re.compile(r'^https?://')
    if re_scheme.match(url):
        filename = re_path.sub('-', re_scheme.sub('', valid_url))
    else:
        url, ext = os.path.splitext(url)
        filename = re_path.sub('-',  url) + ext
    return filename


def has_ext(url: str) -> bool:
    return bool(os.path.splitext(url)[1])


def url_normalize(url: str) -> str:
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
    return url


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
    return urljoin(url, '/')
