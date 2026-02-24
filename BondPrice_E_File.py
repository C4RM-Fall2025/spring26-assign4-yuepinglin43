def getBondPrice_E(face, couponRate, yc):
    bondPrice = 0
    coupon = face * couponRate
    for t, y in enumerate(yc, start=1):
        if t == len(yc):
            cf = face + coupon
        else:
            cf = coupon
        pvm = (1 + y) ** -t
        bondPrice += cf * pvm
    return(bondPrice)

