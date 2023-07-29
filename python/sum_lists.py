# sum all the numbers in a 2-D list


def sum_lists(a_2d_list):
    sum = 0
    for alist in a_2d_list:
        for num in alist:
            sum += num
    return sum
