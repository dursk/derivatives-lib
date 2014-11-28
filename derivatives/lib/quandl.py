import csv
import os
from decimal import Decimal

import requests
import pandas as pd

from auth import AUTH_TOKEN


QUANDL_BASE_URL = 'http://quandl.com/api/v1/datasets'


def get(contract, start=None, end=None, collapse=None, column=None):
    url = '{}/{}.csv?auth_token={}'.format(
        QUANDL_BASE_URL, contract, AUTH_TOKEN
    )
    if start:
        url = '{}&trim_start={}'.format(url, start)
    if end:
        url = '{}&trim_end={}'.format(url, end)
    if collapse:
        url = '{}&collapse={}'.format(url, collapse)
    if column:
        url = '{}&column={}'.format(url, column)
    r = requests.get(url)
    with open('test.csv', 'wb') as csvfile:
        csvfile.write(r.text)
    data = pd.read_csv('test.csv')
    os.remove('test.csv')
    data.index = pd.to_datetime(data.pop('Date'))
    data = data.sort()
    return data
