"""Testing text output mod."""
from page_loader.engine import generate_name

URL = 'https://ru.hexlet.io/courses'
OUTPUT_PATH = '/var/tmp'
CORRECT_NAME = '/var/tmp/ru-hexlet-io-courses.html'


def test_generate_name():
    assert generate_name(URL, OUTPUT_PATH) == CORRECT_NAME
