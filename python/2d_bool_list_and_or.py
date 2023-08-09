## if and, check if lists are all True, if or, check if at least one True


def two_dimensional_booleans(a_superlist, use_and):
    result_list = []
    for list in a_superlist:
        if use_and:
            result_list.append(False not in list)
        else:
            result_list.append(True in list)
    return result_list
