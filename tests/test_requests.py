import tempfile

from page_loader import engine
from page_loader import constants

BASE_TEMP_PATH = tempfile.TemporaryDirectory(suffix='test_requests')


def read_file(path):
    with open(path) as file:
        return file.read()


def test_request_response():
    response = engine.get_page(constants.URL)
    assert response is not None


def test_mock_response(requests_mock):
    with open(constants.HEXLET_PAGE) as fixture:
        requests_mock.get(constants.URL, text=fixture.read())
        response = engine.get_page(constants.URL)

    assert response == read_file(constants.HEXLET_PAGE)


# def test_mock_download(requests_mock):
    # with open(constants.HEXLET_PAGE) as fixture:
        # requests_mock.get(constants.URL, text=fixture.read())    # noqa: 116
        # temp_page = engine.download(constants.URL, BASE_TEMP_PATH.name)  # noqa: 116
        # print(BASE_TEMP_PATH.name)    # noqa: 116
        # data = read_file(temp_page)   # noqa: 116

    # assert data == read_file(constants.PARSED_HEXLET_PAGE)
