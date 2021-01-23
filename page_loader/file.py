import logging
import os
from typing import Union

DIRECTORY_ACCESS_RIGHTS = 0o755


logger = logging.getLogger('base')


def write(data: Union[str, bytes], file_path: str) -> None:
    dir_path = os.path.dirname(file_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path, DIRECTORY_ACCESS_RIGHTS)
        logger.debug(f'directory {dir_path} was created')

    mode, encoding = ('w', 'utf8') if isinstance(data, str) else ('wb', None)
    with open(file_path, mode=mode, encoding=encoding) as f:
        f.write(data)


def read(file_path):
    with open(file_path) as file:
        return file.read()
