import os

import pytest
from bs4 import BeautifulSoup

from traininfojp import RailDetails
from traininfojp import RailList
from traininfojp import RailSummary
from traininfojp import TRAIN_INFO_URL


def test_file(filename):
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'test_files',
    )
    with open(os.path.join(path, filename), 'r') as f:
        return f.read()


@pytest.fixture(scope='module')
def rail_list_html():
    return test_file('rail_list.html')


@pytest.fixture
def rail_list():
    rail_list = RailList()
    return rail_list


@pytest.fixture
def rail_list_init(rail_list_html):
    rail_list = RailList()
    rail_list.parsed_html = BeautifulSoup(rail_list_html, 'html.parser')
    return rail_list


@pytest.fixture(scope='module')
def rail_summary_html():
    return test_file('rail_summary.html')


@pytest.fixture
def rail_summary():
    rail_summary = RailSummary(TRAIN_INFO_URL)
    return rail_summary


@pytest.fixture
def rail_summary_init(rail_summary_html):
    rail_summary = RailSummary(TRAIN_INFO_URL)
    rail_summary.parsed_html = BeautifulSoup(rail_summary_html, 'html.parser')
    return rail_summary


@pytest.fixture(scope='module')
def rail_details_html():
    return test_file('rail_details.html')


@pytest.fixture
def rail_details():
    rail_details = RailDetails(TRAIN_INFO_URL)
    return rail_details


@pytest.fixture
def rail_details_init(rail_details_html):
    rail_details = RailDetails(TRAIN_INFO_URL)
    rail_details.parsed_html = BeautifulSoup(rail_details_html, 'html.parser')
    return rail_details
