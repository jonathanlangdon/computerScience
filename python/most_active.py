# return most active name in a dictionary


def most_active(adict):
    highest = ("", 0)
    for name, days in adict.items():
        if days > highest[1]:
            highest = (name, days)
    return highest[0]
