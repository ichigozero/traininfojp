import re
import urllib.parse

import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://transit.yahoo.co.jp'
TRAIN_INFO_URL = 'https://transit.yahoo.co.jp/traininfo/top'


def _exc_attr_err(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except AttributeError:
            return None

    return wrapper


class TrainType:
    REGULAR = 0
    BULLET_TRAIN = 1
    RAPID = 2


class RailList:
    def __init__(self):
        self.parsed_html = None
        self.fetch_status = ''

    def fetch_parse_html_source(self):
        try:
            global TRAIN_INFO_JP_URL
            response = requests.get(TRAIN_INFO_URL)
            self.parsed_html = BeautifulSoup(response.text, 'html.parser')
            self.fetch_status = 'OK'
        except requests.exceptions.RequestException:
            self.fetch_status = 'ERR'

    def get_regular_train_summary_page_urls(self):
        return self._get_train_page_urls(TrainType.REGULAR)

    def get_bullet_train_details_page_urls(self):
        return self._get_train_page_urls(TrainType.BULLET_TRAIN)

    def get_rapid_train_summary_page_urls(self):
        return self._get_train_page_urls(TrainType.RAPID)

    @_exc_attr_err
    def _get_train_page_urls(self, train_type):
        div = self.parsed_html.find('div', class_='elmTblLstTrain')
        ul = div.find_all('ul')[train_type]
        train_urls = list()

        for li in ul.find_all('li'):
            anchor = li.find('a')
            train_urls.append({
                'title': anchor.text,
                'url': urllib.parse.urljoin(BASE_URL, anchor['href'])
            })

        return train_urls


class RailSummary:
    def __init__(self, page_url):
        self.page_url = page_url
        self.parsed_html = None
        self.fetch_status = ''

    def fetch_parse_html_source(self):
        try:
            response = requests.get(self.page_url)
            self.parsed_html = BeautifulSoup(response.text, 'html.parser')
            self.fetch_status = 'OK'
        except requests.exceptions.RequestException:
            self.fetch_status = 'ERR'

    @_exc_attr_err
    def get_rail_company_names(self):
        names = list()

        for h3 in self.parsed_html.find_all('h3', class_='title'):
            names.append(h3.text)

        return names

    @_exc_attr_err
    def get_line_names_by_rail_company(self, company_name):
        div = self.parsed_html.find(
            'h3', class_='title', string=company_name).parent
        next_div = div.find_next_sibling('div', class_='elmTblLstLine')

        names = list()

        for anchor in next_div.find_all('a'):
            names.append(anchor.text)

        return names

    @_exc_attr_err
    def get_line_status(self, line_name):
        td = self.parsed_html.find('td', string=line_name)
        next_td = td.find_next_sibling()

        if next_td.find('span', class_=re.compile('icn.*')) is not None:
            return next_td.contents[1].text

        return next_td.text

    @_exc_attr_err
    def get_line_status_details(self, line_name):
        td = self.parsed_html.find('td', string=line_name)
        next_td = td.find_next_sibling().find_next_sibling()

        return next_td.text


class RailDetails:
    def __init__(self, page_url):
        self.page_url = page_url
        self.parsed_html = None
        self.fetch_status = ''

    def fetch_parse_html_source(self):
        try:
            response = requests.get(self.page_url)
            self.parsed_html = BeautifulSoup(response.text, 'html.parser')
            self.fetch_status = 'OK'
        except requests.exceptions.RequestException:
            self.fetch_status = 'ERR'
