# Using a nested loop to create a multiplcation table

mystery_int = 5

for num1 in range(1, mystery_int + 1):
    for num2 in range(1, mystery_int + 1):
        print(num1 * num2, "", end="\t")
    print()
