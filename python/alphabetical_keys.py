# return dictionary as a long string after being sorted


def alphabetical_keys(adict):
    user_data = []
    for name, days in adict.items():
        user_data.append((name, days))
    user_data = sorted(user_data, key=lambda x: x[0])
    data_string = ""
    for name, days in user_data:
        data_string += f"{name}: {days}\n"
    return data_string
