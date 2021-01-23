from page_loader.file import read
from page_loader.html_builder import get_modified_page
from page_loader.engine import download
import tempfile

URL = 'https://ru.hexlet.io/courses'
DIR_PATH = '/var/tmp'
MINIMAL_PAGE = 'tests/fixtures/minimal_page.html'
PARSED_MINIMAL_PAGE = 'tests/fixtures/parsed_minimal_page.html'

BASE_TEMP_PATH = tempfile.TemporaryDirectory(suffix='test_requests')
HEXLET_PAGE = 'tests/fixtures/ru-hexlet-io-courses.html'
PARSED_HEXLET_PAGE = 'tests/fixtures/parsed_ru-hexlet-io-courses.html'


def test_get_modified_page():
    modified_page, _ = get_modified_page(URL, read(MINIMAL_PAGE), DIR_PATH)
    assert modified_page == read(PARSED_MINIMAL_PAGE)


def est_mock_download(requests_mock):
    with open(HEXLET_PAGE) as fixture:
        requests_mock.get(URL, text=fixture.read())
        temp_page = download(URL, BASE_TEMP_PATH.name)
        data = read(temp_page)

    assert data == read(PARSED_HEXLET_PAGE)
