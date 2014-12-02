from decimal import Decimal

import pandas as pd

from lib import quandl, helpers


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
    collapse, diff_length = helpers.get_collapse(diff_length)
    start = helpers.convert_start_date(start, diff_length)
    data = _get_data(
        contract, start=start, end=end, collapse=collapse
    )
    diffs = pd.Series()
    for i in xrange(diff_length, len(data)):
        diffs[data.index[i]] = data[i] - data[i - diff_length]
    return diffs
