import tempfile

import requests
import requests_mock

from page_loader import engine

HEXLET_MOCK = 'tests/fixtures/ru-hexlet-io-courses.html'
HEXLET_URL = 'https://ru.hexlet.io/courses'
HEXLET_TEMP_PATH = tempfile.TemporaryDirectory('HEXLET')
HEXLET_TEMP_FILE = engine.download(HEXLET_URL, HEXLET_TEMP_PATH.name)


def read_file(file_path):
    with open(file_path) as file:
        return file.read()


with open(HEXLET_MOCK) as hexlet_mock_data:
    with requests_mock.Mocker() as mock_request:
        mock_request.get(HEXLET_URL, text=hexlet_mock_data.read())
        response = requests.get(HEXLET_URL).text

    print(read_file(HEXLET_TEMP_FILE))
    assert response == read_file(HEXLET_TEMP_FILE)
