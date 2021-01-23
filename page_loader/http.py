import logging
from typing import Optional

import requests
from requests import Response

CHROME_DESKTOP = """mozilla/5.0 (windows nt 10.0; win64; x64) \
applewebkit/537.36 (khtml, like gecko) chrome/71.1.2222.33 safari/537.36"""
TIMEOUT = 1


logger = logging.getLogger('base')


def get_data(url: str) -> Optional[Response]:
    headers = {'user-agent': CHROME_DESKTOP}
    try:
        logger.debug(f'get {url}')
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
    except requests.exceptions.ReadTimeout:
        logger.error(f'ReadTimeout, timeout = {TIMEOUT}')
    else:
        if response.ok:
            return response
        else:
            logger.exception(f'http response: {response.status_code}, Requested page: {url}')  # noqa: E501
