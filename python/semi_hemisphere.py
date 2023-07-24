# with an input latitude and longitude output a semihemisphere


def semihemisphere(lat, long):
    semi = ""
    if lat > 0:
        semi += "North"
    else:
        semi += "South"
    if long > 0:
        semi += "east"
    else:
        semi += "west"
    return semi
