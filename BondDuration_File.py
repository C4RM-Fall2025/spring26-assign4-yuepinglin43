def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    pvcf_sum = 0
    coupon = couponRate * face
    for t in range(1, m + 1):
        if t == m:
            cf = coupon + face
        else:
            cf = coupon
        pvm = ((1 + y) ** -t)
        pvcf = pvm * cf
        pvcf_sum += pvcf
        pvcfsum += pvcf * t
    bondDuration = pvcfsum / pvcf_sum


    return(bondDuration)


y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
duration = getBondDuration(y, face, couponRate, m, ppy = 1)
print(duration)
