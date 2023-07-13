# an example of debugging loops - this is totally wrong
""" The initial bad code
num = 5
result = 1
for i in range(num):
    result *= i
print(result)
"""

""" A way to debug and find where the code went wrong using print to console
num = 5
result = 1
for i in range(num):
    print(i, result)
    result *= i
print(result)
"""

# final solution

num = 4
result = 1
for i in range(1, num + 1):
    result *= i
print(result)
