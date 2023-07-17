# function with 2 date parameters to determine what season it is


def what_season(month, day):
    months = {
        "January": {range(1, 32): "Winter"},
        "February": {range(1, 30): "Winter"},
        "March": {range(1, 20): "Winter", range(20, 32): "Spring"},
        "April": {range(1, 31): "Spring"},
        "May": {range(1, 32): "Spring"},
        "June": {range(1, 21): "Spring", range(21, 31): "Summer"},
        "July": {range(1, 32): "Summer"},
        "August": {range(1, 32): "Summer"},
        "September": {range(1, 22): "Summer", range(22, 31): "Fall"},
        "October": {range(1, 32): "Fall"},
        "November": {range(1, 31): "Fall"},
        "December": {range(1, 21): "Fall", range(21, 32): "Winter"},
    }

    for month_name, days in months.items():
        for day_range, season in days.items():
            if month == month_name and day in day_range:
                return season

    return "Invalid input"


print(what_season("March", 18))
