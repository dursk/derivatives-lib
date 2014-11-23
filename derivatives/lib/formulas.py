import math
from decimal import Decimal


def discrete_compound(principal, rate, term, compound_period):
    return principal * math.pow(
        1 + (rate/compound_period),
        int(term * compound_period)
    )

def continuous_compound(principal, rate, term):
    return principal * math.exp(rate * term)

def discrete_to_continuous(rate, compound_period):
    return compound_period * math.log(1 + (rate/compound_period))

def continuous_to_discrete(rate, compound_period):
    return compound_period * (math.exp(rate/compound_period) - 1)
