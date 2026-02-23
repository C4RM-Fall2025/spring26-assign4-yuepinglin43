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


y = 0.03
face = 2000000
couponRate = 0.04
m = 10

price1 = getBondPrice (y, face, couponRate, m, ppy=1)
print(price1)
price2 = getBondPrice (y, face, couponRate, m, ppy=2)
print(price2)

