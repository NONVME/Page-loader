from page_loader.parser import parse
import page_loader.constants as ct


def read(path):
    with open(path) as file:
        return file.read()


def test_parsing():
    assert parse(ct.URL, read(ct.MINIMAL_PAGE),
                 ct.DIR_PATH) == read(ct.PARSED_MINIMAL_PAGE)
