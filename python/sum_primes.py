# find the sum of all prime numbers leading up to a given inputed integer


def is_prime(n):
    from itertools import count, islice

    return n > 1 and all(n % i for i in islice(count(2), int(n**0.5) - 1))


# first solved with a for-loop

# def sum_of_primes(num):
#     sum = 0
#     for i in range(2, num + 1):
#         if is_prime(i):
#             sum += i
#     return sum


def sum_of_primes(num):
    sum = 0
    i = 2
    while i <= num:
        if is_prime(i):
            sum += i
        i += 1
    return sum
