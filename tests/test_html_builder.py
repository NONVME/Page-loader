import tempfile

from page_loader.engine import download
from page_loader.file import read
from page_loader.html_builder import process_html


def test_get_modified_page():
    URL = 'https://ru.hexlet.io/courses'
    MINIMAL_PAGE = 'tests/fixtures/minimal_page.html'
    PARSED_MINIMAL_PAGE = 'tests/fixtures/parsed_minimal_page.html'
    modified_page, _ = process_html(URL, read(MINIMAL_PAGE))
    assert modified_page == read(PARSED_MINIMAL_PAGE)


def test_mock_download(requests_mock):
    URL = 'https://ru.hexlet.io/courses'
    ASSET = 'https://ru.hexlet.io/lessons.rss'
    BASE_TEMP_PATH = tempfile.TemporaryDirectory()
    HEXLET_PAGE = 'tests/fixtures/ru-hexlet-io-courses.html'
    PARSED_HEXLET_PAGE = 'tests/fixtures/parsed_ru-hexlet-io-courses.html'

    with open(HEXLET_PAGE) as fixture:
        requests_mock.get(URL, text=fixture.read())
        requests_mock.get(ASSET, text='')
        temp_page = download(URL, BASE_TEMP_PATH.name)
        data = read(temp_page)

    assert data == read(PARSED_HEXLET_PAGE)
