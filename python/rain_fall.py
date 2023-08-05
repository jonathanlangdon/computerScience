# take a list of data and return average up to -1 input


def average_rainfall(daily_rain):
    total = 0
    count = 0
    for rain in daily_rain:
        if rain == -1:
            break
        else:
            total += rain
            count += 1
    return total / count
