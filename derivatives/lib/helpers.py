from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_collapse(diff_length):
    collapse = 'monthly'
    if diff_length >= 3:
        collapse = 'quarterly'
        diff_length = diff_length / 3
    return collapse, diff_length

def convert_start_date(date, diff_length):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date - relativedelta(day=1)
    date = date - timedelta(days=183)
    return str(date)
