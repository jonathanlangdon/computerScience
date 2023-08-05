# take a list of data and return geometric average


def geometric_rainfall(daily_rain):
    product = 1
    count = 0
    for rain in daily_rain:
        if rain == -1:
            break
        else:
            product *= rain
            count += 1
    return product ** (1 / count)
