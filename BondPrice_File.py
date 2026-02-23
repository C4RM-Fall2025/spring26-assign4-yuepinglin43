def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0
    for t in range(1, n + 1):
        pvm = (1 + r) ** -t
        bondPrice += pvm * coupon
    bondPrice += face * (1 + r) ** -n
    return(bondPrice)


