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


def test_get_regular_train_summary_page_urls(rail_list, rail_list_init):
    output_1 = rail_list.get_regular_train_summary_page_urls()

    assert output_1 is None

    output_2 = rail_list_init.get_regular_train_summary_page_urls()

    first_expected_val = {
        'title': '北海道',
        'url': 'https://transit.yahoo.co.jp/traininfo/area/2/'
    }
    last_expected_val = {
        'title': '九州',
        'url': 'https://transit.yahoo.co.jp/traininfo/area/7/'
    }

    assert output_2[0] == first_expected_val
    assert output_2[-1] == last_expected_val


def test_get_bullet_train_details_page_urls(rail_list, rail_list_init):
    output_1 = rail_list.get_bullet_train_details_page_urls()

    assert output_1 is None

    output_2 = rail_list_init.get_bullet_train_details_page_urls()

    first_expected_val = {
        'title': '北海道新幹線',
        'url': 'https://transit.yahoo.co.jp/traininfo/detail/637/0/'
    }
    last_expected_val = {
        'title': '九州新幹線',
        'url': 'https://transit.yahoo.co.jp/traininfo/detail/410/0/'
    }

    assert output_2[0] == first_expected_val
    assert output_2[-1] == last_expected_val
