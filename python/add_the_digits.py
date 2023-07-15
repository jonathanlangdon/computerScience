a_string = "F1#2daDv^f%$G$25Fd"

sum = 0

for char in a_string:
    if char.isdigit():
        sum += int(char)

print(sum)
