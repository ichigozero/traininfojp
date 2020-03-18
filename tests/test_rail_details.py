import requests
from bs4 import BeautifulSoup

from traininfojp import TRAIN_INFO_URL


def test_fetch_parse_html_source(requests_mock, rail_details,
                                 rail_details_html):
    requests_mock.get(TRAIN_INFO_URL, text=rail_details_html)
    rail_details.fetch_parse_html_source()

    expected_html = BeautifulSoup(rail_details_html, 'html.parser')
    assert rail_details.parsed_html == expected_html
    assert rail_details.fetch_status == 'OK'


def test_failed_fetch_parse_html_source(requests_mock, rail_details,
                                        rail_details_html):
    requests_mock.get(TRAIN_INFO_URL, exc=requests.exceptions.HTTPError)
    rail_details.fetch_parse_html_source()

    assert rail_details.parsed_html is None
    assert rail_details.fetch_status == 'ERR'


def test_get_line_kanji_name(rail_details, rail_details_init):
    assert rail_details.get_line_kanji_name() is None
    assert rail_details_init.get_line_kanji_name() == '芝山鉄道線'


def test_get_line_kana_name(rail_details, rail_details_init):
    assert rail_details.get_line_kana_name() is None
    assert rail_details_init.get_line_kana_name() == 'しばやまてつどうせん'


def test_get_line_status(rail_details, rail_details_init):
    assert rail_details.get_line_status() is None
    assert rail_details_init.get_line_status() == '平常運転'


def test_get_line_status_details(rail_details, rail_details_init):
    expected_1 = None
    expected_2 = '現在､事故･遅延に関する情報はありません。'

    assert rail_details.get_line_status_details() is expected_1
    assert rail_details_init.get_line_status_details() == expected_2
