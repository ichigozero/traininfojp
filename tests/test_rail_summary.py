import requests
from bs4 import BeautifulSoup

from traininfojp import TRAIN_INFO_URL


def test_fetch_parse_html_source(requests_mock, rail_summary,
                                 rail_summary_html):
    requests_mock.get(TRAIN_INFO_URL, text=rail_summary_html)
    rail_summary.fetch_parse_html_source()

    expected_html = BeautifulSoup(rail_summary_html, 'html.parser')
    assert rail_summary.parsed_html == expected_html
    assert rail_summary.fetch_status == 'OK'


def test_failed_fetch_parse_html_source(requests_mock, rail_summary,
                                        rail_summary_html):
    requests_mock.get(TRAIN_INFO_URL, exc=requests.exceptions.HTTPError)
    rail_summary.fetch_parse_html_source()

    assert rail_summary.parsed_html is None
    assert rail_summary.fetch_status == 'ERR'
