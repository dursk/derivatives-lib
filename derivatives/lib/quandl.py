import csv
import os

import requests
import pandas as pd

from auth import AUTH_TOKEN


QUANDL_BASE_URL = 'http://quandl.com/api/v1/datasets'


def get(contract, start=None, end=None):
    url = '{}/{}.csv?auth_token={}'.format(
        QUANDL_BASE_URL, contract, AUTH_TOKEN
    )
    if start:
        url = '{}&trim_start={}'.format(url, start)
    if end:
        url = '{}&trim_end={}'.format(url, end)
    print url
    r = requests.get(url)
    with open('test.csv', 'wb') as csvfile:
        csvfile.write(r.text)
    data = pd.read_csv('test.csv')
    os.remove('test.csv')
    return data
