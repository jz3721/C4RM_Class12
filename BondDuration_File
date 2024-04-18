import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    coupon = face * couponRate / ppy
    periods = np.arange(1, m * ppy + 1)
    cash_flows = np.full(m * ppy, coupon)
    cash_flows[-1] += face
    discount_factors = (1 + y / ppy) ** periods
    present_values = cash_flows / discount_factors
    weighted_times = periods * present_values
    bond_duration = np.sum(weighted_times) / np.sum(present_values)
    
    return bond_duration
