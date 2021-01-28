import logging
from typing import Optional

import requests
from requests import Response

TIMEOUT = 1


logger = logging.getLogger('base_console')


def get_data(url: str) -> Optional[Response]:
    try:
        logger.debug(f'get {url}')
        response = requests.get(url, timeout=TIMEOUT)
    except requests.exceptions.ReadTimeout:
        logger.error(f'ReadTimeout, timeout = {TIMEOUT}')
    else:
        if response.ok:
            return response
        else:
            logger.exception(f'http response: {response.status_code}, Requested page: {url}')  # noqa: E501
