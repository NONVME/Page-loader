import tempfile

from page_loader import engine
from page_loader import constants

BASE_TEMP_PATH = tempfile.TemporaryDirectory('test_requests')


def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def test_request_response():
    response = engine.get_page(constants.BASE_URL)
    assert response is not None


def test_mock_response(requests_mock):
    with open(constants.BASE_FIXTURE) as fixture:
        requests_mock.get(constants.BASE_URL, text=fixture.read())
        response = engine.get_page(constants.BASE_URL).text

    assert response == read_file(constants.BASE_FIXTURE)


def test_mock_download(requests_mock):
    with open(constants.BASE_FIXTURE) as fixture:
        requests_mock.get(constants.BASE_URL, text=fixture.read())
        temp_file = engine.download(constants.BASE_URL, BASE_TEMP_PATH.name)
        data = read_file(temp_file)

    assert data == read_file(constants.BASE_FIXTURE)
