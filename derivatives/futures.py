import math
from decimal import Decimal

import requests
import numpy as np
import pandas as pd

from lib import formulas, quandl

MONTHS = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']

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

def get_oil_vs_6month_rate(start, end):
    oil_data = None
    formatted_start = '{}-01-01'.format(start)
    formatted_end = '{}-12-31'.format(end)
    for year in xrange(start, end+1):
        for month in MONTHS:
            oil_contract = 'CME/B{}{}'.format(month, year)
            data = quandl.get(oil_contract)
            oil_data = pd.concat([oil_data, data])
    interest_data = quandl.get(
        'FRED/DTB6',
        start=formatted_start,
        end=formatted_end
    )
    return oil_data, interest_data
