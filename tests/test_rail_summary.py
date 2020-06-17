import requests
from bs4 import BeautifulSoup

from traininfojp import TRAIN_INFO_URL


def test_fetch_parse_html_source(requests_mock, rail_summary,
                                 rail_summary_html):
    requests_mock.get(TRAIN_INFO_URL, text=rail_summary_html)
    rail_summary.fetch_parse_html_source(TRAIN_INFO_URL)

    expected_html = BeautifulSoup(rail_summary_html, 'html.parser')
    assert rail_summary._parsed_html == expected_html
    assert rail_summary.fetch_status == 'OK'


def test_failed_fetch_parse_html_source(requests_mock, rail_summary):
    requests_mock.get(TRAIN_INFO_URL, exc=requests.exceptions.HTTPError)
    rail_summary.fetch_parse_html_source(TRAIN_INFO_URL)

    assert rail_summary._parsed_html is None
    assert rail_summary.fetch_status == 'ERR'


def test_get_rail_company_names(rail_summary, rail_summary_init):
    output_1 = rail_summary.get_rail_company_names()

    assert output_1 is None

    output_2 = rail_summary_init.get_rail_company_names()

    assert output_2[0] == 'JR東日本'
    assert output_2[-1] == '芝山鉄道'


def test_get_line_names_by_rail_company(rail_summary, rail_summary_init):
    output_1 = rail_summary.get_line_names_by_rail_company('JR東日本')

    assert output_1 is None

    output_2 = rail_summary_init.get_line_names_by_rail_company('JR東日本')

    assert output_2[0] == '山手線'
    assert output_2[-1] == '上野東京ライン'


def test_get_line_status(rail_summary, rail_summary_init):
    assert rail_summary.get_line_status('山手線') is None
    assert rail_summary.get_line_status('横浜線') is None

    assert rail_summary_init.get_line_status('山手線') == '平常運転'
    assert rail_summary_init.get_line_status('横浜線') == '平常運転'


def test_get_line_status_details(rail_summary, rail_summary_init):
    expected_1 = None
    expected_2 = '埼京川越線内で線路内点検を行った...'

    assert rail_summary.get_line_status_details('山手線') is expected_1
    assert rail_summary_init.get_line_status_details('山手線') == expected_2


def test_get_line_details_page_url(rail_summary, rail_summary_init):
    expected_1 = None
    expected_2 = 'https://transit.yahoo.co.jp/traininfo/detail/21/0/'

    assert rail_summary.get_line_details_page_url('山手線') is expected_1
    assert rail_summary_init.get_line_details_page_url('山手線') == expected_2
