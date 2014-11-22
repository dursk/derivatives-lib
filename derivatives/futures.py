from decimal import Decimal

from lib import formulas

def forward_contract_payoff(delivery_price, spot_price, short=False):
    delivery_price = Decimal(str(delivery_price))
    spot_price = Decimal(str(spot_price))
    if short:
        return delivery_price - spot_price
    return spot_price - delivery_price

