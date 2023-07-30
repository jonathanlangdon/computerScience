# try-catch but only checking for zero division

mystery_value = "5"

try:
    print(10 / mystery_value)
except ZeroDivisionError:
    print("Not possible")
