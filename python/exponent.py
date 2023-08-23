# use recursion to calculate exponent


def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return exponent_calc(base, expo - 1) * base


print(exponent_calc(5, 3))
# prints 125
