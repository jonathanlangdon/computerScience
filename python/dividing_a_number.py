# try 3 different operations on a number

mystery_value = 3

try:
    print(mystery_value / mystery_value)
except:
    try:
        print(mystery_value / (mystery_value + 5))
    except:
        try:
            print(mystery_value * 5)
        except:
            pass
