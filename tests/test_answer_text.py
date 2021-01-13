"""Testing text output modформатирование."""
import page_loader.constants as ct
from page_loader.formaters import generate_name_page
from page_loader.formaters import url_formatting
from page_loader.formaters import link_formatting


def test_generate_name_page():
    assert generate_name_page(tail_path=ct.URL,
                              forepart_path=ct.DIR_PATH,
                              end_of_path='.html') == ct.CONVERTED_FILE_NAME


def test_url_formatting():
    assert url_formatting(ct.URL) == ct.CONVERTED_URL


def test_link_formatting():
    assert link_formatting(ct.LINK) == (ct.CONVERTED_LINK_PATH,
                                        ct.CONVERTED_LINK_EXT)
