# get ordinal (1st, 2nd, etc) given the integer


def to_ordinal(integer):
    ordinals = {0: "th", 1: "st", 2: "nd", 3: "rd"}
    last_digit = int(str(integer)[-1])
    if last_digit > 3 or integer in [11, 12, 13]:
        return str(integer) + "th"
    else:
        return str(integer) + ordinals[last_digit]
