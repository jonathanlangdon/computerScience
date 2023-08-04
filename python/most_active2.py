# return most active name from a list of dictionaries


def most_active(list_o_dict):
    highest = ("", 0)
    for dict in list_o_dict:
        if dict["days_active"] > highest[1]:
            highest = (dict["name"], dict["days_active"])
    return highest[0]
