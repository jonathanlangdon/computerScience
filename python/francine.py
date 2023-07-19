#


def francine(num):
    count = 0
    while num > 2:
        if num % 3 == 0:
            num //= 3
            count += 1
            continue
        elif (num - 1) % 3 == 0:
            num += 2
            count += 1
            continue
        elif (num - 2) % 3 == 0:
            num *= 2
            count += 1
            continue

    return count


print(francine(50))
print(francine(15))
print(francine(124))
