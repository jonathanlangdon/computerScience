# returns todays date in a particular format

from datetime import date


def get_todays_date():
    return f"{date.today().year}/{date.today().month}/{date.today().day}"


print(get_todays_date())
