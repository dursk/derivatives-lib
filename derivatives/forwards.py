import math
from decimal import Decimal

from lib import formulas

def forward_contract_payoff(delivery_price, spot_price, short=False):
    delivery_price = Decimal(str(delivery_price))
    spot_price = Decimal(str(spot_price))
    if short:
        return delivery_price - spot_price
    return spot_price - delivery_price

def get_forward_price(risk_free_rate, current_price, time_to_maturity,
                      known_income=0, known_yield=0):
    return (current_price - known_income) * math.exp(
        (risk_free_rate - known_yield) * time_to_maturity
    )

def get_forward_value(delivery_price, spot_price, risk_free_rate,
                      time_to_maturity, known_income=0, known_yield=0):
    x = spot_price * math.exp(-known_yield * time_to_maturity)
    y = delivery_price * math.exp(-risk_free_rate * time_to_maturity)
    return x - known_income - y
