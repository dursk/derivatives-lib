from lib import formulas

# paid option_price to buy at strike
def long_call(current, strike, option_price):
    if current > strike:
        # buy at strike and sell at current
        return current - strike - option_price
    else:
        return -option_price

# paid option_price to sell at strike
def long_put(current, strike, option_price):
    if strike > current:
        # buy at current and sell at strike
        return strike - current - option_price
    else:
        return -option_price

# received option_price but have to sell at strike
def short_call(current, strike, option_price):
    if strike > current:
        return option_price
    # buy at current and sell at strike
    return strike - current + option_price

# received option_price but have to buy at strike
def short_put(current, strike, option_price):
    if strike < current:
        # he's never making me buy if I get a good deal
        return option_price
    # buy at strike and sell at current
    return current - strike + option_price
