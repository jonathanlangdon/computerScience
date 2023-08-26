# calculates the maximum number of searches required with a binary search


def max_binary(num):
    if num == 1:
        return 1
    return 1 + max_binary(num // 2)


print(max_binary(9987))
