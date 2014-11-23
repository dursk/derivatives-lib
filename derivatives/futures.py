import math
from decimal import Decimal

from lib import formulas

def get_fixed_storage_cost(storage_cost, risk_free_rate, term):
    return storage_cost * math.exp(-risk_free_rate * term)

def get_commodities_price(spot_price, risk_free_rate, term, storage_cost=0,
                          convienence_yield=0, fixed_storage_cost=False):
    if fixed_storage_cost:
        return (spot_price + get_fixed_storage_cost(
            storage_cost, risk_free_rate, term
        )) * math.exp(risk_free_rate * term)
    return spot_price * math.exp((risk_free_rate + storage_cost) * term)

def get_futures_price(spot_price, risk_free_rate, term, cost_of_carry,
                      convenience_yield=0):
    return spot_price * math.exp((cost_of_carry - convenience_yield) * term)
