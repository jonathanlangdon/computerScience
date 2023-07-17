# determine if an inputed year is a leap year or not


def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        else:
            return not year % 100 == 0
    else:
        return False
