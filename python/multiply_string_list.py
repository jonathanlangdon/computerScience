# practice modifying a list with loops


def multiply_strings(list1):
    for i in range(0, len(list1)):
        if i % 2 == 0:
            list1[i] = list1[i] * 2
        if i % 3 == 0:
            list1[i] = list1[i] * 3
    return list1
