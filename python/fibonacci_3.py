# use recursion to make an altered Fibonacci sequenc of the previous 3 numbers


def fib3(num):
    if num <= 3:
        return 1
    else:
        return fib3(num - 1) + fib3(num - 2) + fib3(num - 3)


# The lines below will test your code. If your funciton is
# correct, they will print 1, 3, 17, and 57.
print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(9))
