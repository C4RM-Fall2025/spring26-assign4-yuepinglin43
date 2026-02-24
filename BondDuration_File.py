def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    rate_per_period = y / ppy
    coupon_per_period = couponRate * face / ppy
    pvcfsum = 0
    pv_sum = 0
    
    for t in range(1, periods + 1):
        if t == periods:
            cf = coupon_per_period + face
        else:
            cf = coupon_per_period
        pv = cf / ((1 + rate_per_period) ** t)
        pv_sum += pv
        pvcfsum += pv * t
    bondDuration = (pvcfsum / pv_sum) / ppy
    return(bondDuration)


y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
