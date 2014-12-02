import math
from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta

import requests
import numpy as np
import pandas as pd

from lib import formulas, quandl, helpers
from data import contracts

MONTHS = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']
QUARTERS = {
    'H': '03-31',
    'M': '06-30',
    'U': '09-30',
    'Z': '12-31'
}

def get_fixed_storage_cost(storage_cost, risk_free_rate, term):
    return storage_cost * math.exp(-risk_free_rate * term)

def get_price(spot_price, risk_free_rate, term, known_income=0, known_yield=0):
    return (spot_price - known_income) * math.exp(
        (risk_free_rate - known_yield) * term
    )

def get_value(spot_price, delivery_price, risk_free_rate, term,
              known_income=0, known_yield=0):
    return (spot_price * math.exp(-known_yield * term)) - known_income - \
        (delivery_price * math.exp(-risk_free_rate * term))

def _get_data(contract, start=None, end=None, collapse=None):
    data = quandl.get(
        contract, start=start, end=end, collapse=collapse,
        column=6
    )
    return data['Settle'].copy()

def get_quarterly_diffs(contract, diff_length, start, end):
    collapse, diff_length = helpers.get_collapse(diff_length)
    starting_index = contracts.QUARTERLY.index(start)
    ending_index = contracts.QUARTERLY.index(end)
    all_data = pd.Series()
    for i in xrange(starting_index, ending_index + 1):
        current = contracts.QUARTERLY[i]
        end_date = '{}-{}'.format(current[1:], QUARTERS[current[0]])
        start_date = datetime.strptime(end_date, '%Y-%m-%d')
        start_date = start_date - relativedelta(months=6)
        data = _get_data(
            contract + contracts.QUARTERLY[i],
            start=start_date, end=end_date, collapse=collapse
        )
        all_data[data.index[-1]] = data[-1] - data[0]
    return all_data
