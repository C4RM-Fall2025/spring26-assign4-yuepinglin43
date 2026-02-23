def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    m = max(times)
    coupon = face * couponRate
    for t, y in zip(times, yc):
        if t == m:
            cf = coupon + face
        else:
            cf = coupon
        pvm = (1 + y) ** -t
        bondPrice += cf * pvm
    return(bondPrice)


# Test values
yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04
print(getBondPrice_Z(face, couponRate, times, yc))
