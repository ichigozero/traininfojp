import os

import pytest
from bs4 import BeautifulSoup

from traininfojp import RailList


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
