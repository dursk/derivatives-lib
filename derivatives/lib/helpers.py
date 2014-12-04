from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import OrderedDict

QUARTERS = OrderedDict([
    ('H', datetime.strptime('03-31', '%m-%d')),
    ('M', datetime.strptime('06-30', '%m-%d')),
    ('U', datetime.strptime('09-30', '%m-%d')),
    ('Z', datetime.strptime('12-31', '%m-%d'))
])

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

def get_quarter(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    for key, value in QUARTERS.iteritems():
        if date.month <= value.month and date.day <= value.day:
            return key
