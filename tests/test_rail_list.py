import requests
from bs4 import BeautifulSoup

from traininfojp import TRAIN_INFO_URL


def test_fetch_parse_html_source(requests_mock, rail_list,
                                 rail_list_html):
    requests_mock.get(TRAIN_INFO_URL, text=rail_list_html)
    rail_list.fetch_parse_html_source()

    expected_html = BeautifulSoup(rail_list_html, 'html.parser')
    assert rail_list.parsed_html == expected_html
    assert rail_list.fetch_status == 'OK'


def test_failed_fetch_parse_html_source(requests_mock, rail_list,
                                        rail_list_html):
    requests_mock.get(TRAIN_INFO_URL, exc=requests.exceptions.HTTPError)
    rail_list.fetch_parse_html_source()

    assert rail_list.parsed_html is None
    assert rail_list.fetch_status == 'ERR'
