# try-catch block for zero division

mystery_value = 9

try:
    print(10 / mystery_value)
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Not possible")
