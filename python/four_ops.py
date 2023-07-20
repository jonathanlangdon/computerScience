# try 4 operations and do try/catch

a = 4
b = "Score"

try:
    print(round(a + b, 2))
except:
    try:
        print(a + b)
    except:
        print("Error!")
try:
    print(round(a - b, 2))
except:
    try:
        print(a - b)
    except:
        print("Error!")
try:
    print(round(a * b, 2))
except:
    try:
        print(a * b)
    except:
        print("Error!")
try:
    print(round(a / b, 2))
except:
    try:
        print(a / b)
    except:
        print("Error!")
