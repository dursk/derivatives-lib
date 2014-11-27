import csv
import os

import requests
import pandas as pd

QUANDL_BASE_URL = 'http://quandl.com/api/v1/datasets'

def get_futures(contract):
    r = requests.get('{}/{}.csv'.format(QUANDL_BASE_URL, contract))
    with open('test.csv', 'wb') as csvfile:
        csvfile.write(r.text)
    data = pd.read_csv('test.csv')
    os.remove('test.csv')
    return data
