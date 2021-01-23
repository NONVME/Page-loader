from page_loader import engine
from page_loader.file import read

HEXLET_PAGE = 'tests/fixtures/ru-hexlet-io-courses.html'
URL = 'https://ru.hexlet.io/courses'


def test_mock_response(requests_mock):
    with open(HEXLET_PAGE) as fixture:
        requests_mock.get(URL, text=fixture.read())
        response = engine.get_data(URL)

    assert response.text == read(HEXLET_PAGE)
