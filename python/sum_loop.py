mystery_int = -3

mysum = 0
operator = ""

if mystery_int > 0:
    operator = "+"
else:
    operator = "-"

for i in range(0, eval(f"{mystery_int}{operator}1"), eval(f"{operator}1")):
    mysum += i

print(mysum)
