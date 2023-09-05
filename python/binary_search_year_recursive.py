# use recursion to do a binary search to see if any dates in a list are in a year

from datetime import date


def binary_search_year(searchList, searchYear):
    searchList.sort(key=lambda date_obj: date_obj.year)
    min = 0
    max = len(searchList) - 1
    if min <= max:
        currentMiddle = (min + max) // 2
        if searchList[currentMiddle].year == searchYear:
            return True
        elif searchYear < searchList[currentMiddle].year:
            return binary_search_year(searchList[0:currentMiddle], searchYear)
        else:
            return binary_search_year(searchList[currentMiddle + 1 :], searchYear)
    return False


# If your function works correctly, this will originally
# print: True, then False

listOfDates = [
    date(2016, 11, 26),
    date(2014, 11, 29),
    date(2008, 11, 29),
    date(2000, 11, 25),
    date(1999, 11, 27),
    date(1998, 11, 28),
    date(1990, 12, 1),
    date(1989, 12, 2),
    date(1985, 11, 30),
]

print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))
