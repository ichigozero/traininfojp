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
