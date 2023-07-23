# count how many factors a number has


def count_factors(int):
    count = 0
    for i in range(2, int):
        if int % i == 0:
            count += 1
    return count
