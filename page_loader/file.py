import logging
import os
from typing import Union


logger = logging.getLogger('base')


def write(data: Union[str, bytes],
          file_path: str, *, is_assets: bool = False) -> None:
    dir_path = os.path.dirname(file_path)

    if not os.path.exists(dir_path) and is_assets:
        try:
            os.makedirs(dir_path)
            logger.debug(f'directory {dir_path} was created')
        except PermissionError:
            logger.exception(
                f'not enough rights to create the directory {dir_path}'
            )

    mode, encoding = ('w', 'utf8') if isinstance(data, str) else ('wb', None)
    with open(file_path, mode=mode, encoding=encoding) as f:
        f.write(data)


def read(file_path):
    with open(file_path) as file:
        return file.read()
