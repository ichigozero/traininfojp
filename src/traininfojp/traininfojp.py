import requests
from bs4 import BeautifulSoup


TRAIN_INFO_URL = 'https://transit.yahoo.co.jp/traininfo/top'


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
