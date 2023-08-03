# turn a list of tuples into a dictionary


def tup_to_dict(list_o_tuples):
    dict_new = {}
    for tuple in list_o_tuples:
        (val1, val2) = tuple
        dict_new[val1] = val2
    return dict_new
