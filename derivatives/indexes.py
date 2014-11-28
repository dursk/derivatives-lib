from decimal import Decimal

import pandas as pd

from lib import quandl


def _get_data(contract, start=None, end=None, collapse=None):
    data = quandl.get(
        contract, start=start, end=end, collapse=collapse,
        column=4
    )
    return data['Close'].copy()

def get_diffs(contract, diff_length, start=None, end=None):
    """
    Get the price differences for the diff_length
    for a given contract from the start to end date.
    The diff_length param should be an int representing
    the number of months.
    """
    collapse = 'monthly'
    if diff_length >=3:
        collapse = 'quarterly'
        diff_length = diff_length / 3
    data = _get_data(
        contract, start=start, end=end, collapse=collapse
    )
    diffs = pd.Series()
    for i in xrange(diff_length, len(data)):
        diffs[data.index[i]] = data[i] - data[i - diff_length]
    return diffs
