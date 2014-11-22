import math
from decimal import Decimal


def compound_interest(principal, rate, term, compound_period):
    return principal * math.pow(
        1 + (rate/compound_period),
        int(term * compound_period)
    )
