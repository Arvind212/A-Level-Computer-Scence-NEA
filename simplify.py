def simplify(fract):
    fraction = fract.partition("/")
    numerator = int(fraction[0])
    denominator = int(fraction[2])
    negative = False
    remainder = numerator % denominator
    if remainder == 0:
        return str(int(numerator/denominator))
    if numerator < 0 and denominator < 0:
        numerator = numerator * -1
        denominator = denominator * -1
    if numerator < 0 and denominator > 0:
        numerator = numerator * -1
        negative = True
    if denominator < 0 and numerator > 0:
        denominator = denominator * -1
        negative = True
    n_factors = []
    d_factors = []
    common_factors = []
    for i in range(1,(numerator+1)):
        if numerator % i == 0:
            n_factors.append(i)
    for i in range(1,(denominator+1)):
        if denominator % i == 0:
            d_factors.append(i)
    for i in n_factors:
        if i in d_factors:
            common_factors.append(i)
    if len(common_factors) != 0:
        HCF = common_factors[-1]
        answer = f"{int(numerator/HCF)}/{int(denominator/HCF)}"
        if negative == True:
            answer = f"-{answer}"
    else:
        answer = fract
    return answer