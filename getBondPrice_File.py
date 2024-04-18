import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon = face * couponRate / ppy
    cash_flows = np.full(m * ppy, coupon)
    cash_flows[-1] += face
    discount_factors = (1 + y / ppy) ** np.arange(1, m * ppy + 1)
    present_values = cash_flows / discount_factors
    bond_price = np.sum(present_values)
    
    return bond_price
