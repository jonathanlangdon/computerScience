# if and, check if list is all True, if or, check if at least one True


def one_dimensional_booleans(bool_list, use_and):
    if use_and:
        return not False in bool_list
    else:
        return True in bool_list
