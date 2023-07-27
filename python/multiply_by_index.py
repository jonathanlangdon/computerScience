# multiple each item in a list by its index


def multiply_by_index(alist):
    for i in range(0, len(alist)):
        alist[i] *= i
    return alist
