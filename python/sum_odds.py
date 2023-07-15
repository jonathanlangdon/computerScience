# find the sum of all odd numbers from 1 to (exclusive) the mystery num

mystery_int = 10

sum = 0

for i in range(1, mystery_int, 2):
    sum += i

print(sum)
