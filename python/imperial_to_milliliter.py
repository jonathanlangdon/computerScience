# return number of mL from a given imperial volume


def to_metric(text):
    split_list = text.split(" ")
    num = split_list[0]
    unit = split_list[1]
    imperial_units = {
        "gallons": 3785.41,
        "quarts": 946.35,
        "pints": 473.18,
        "cups": 240,
        "ounces": 29.57,
        "tablespoons": 14.79,
        "teaspoons": 4.93,
    }
    return round(float(num) * imperial_units[unit], 2)
