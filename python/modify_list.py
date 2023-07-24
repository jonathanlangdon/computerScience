# various modifications of a list


def modify_list(list1):
    list1.sort()
    list1 = list1[::-1][:-3]
    if 7 in list1:
        list1.remove(7)
    list1[0] = list1[0] * 2
    list1[2] = list1[2] * 2
    return list1
