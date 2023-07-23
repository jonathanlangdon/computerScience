# determine product of all numbers between 2 numbers inclusively

minimum = 2
maximum = 5

result = 1

for i in range(minimum, maximum + 1):
    result *= i

print(result)
