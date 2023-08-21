# two functions that do the same thing, one using recursion


def count_down(start):
    if start <= 0:
        print(start)
    else:
        print(start)
        count_down(start - 1)


def count_down2(start):
    for num in range(start, -1, -1):
        print(num)


count_down2(9)
