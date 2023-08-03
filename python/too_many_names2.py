# make a dictionary of full names with first names in common


def name_lists(names):
    dict_name = {}
    for name in names:
        (first, last) = name.split()
        if first not in dict_name:
            dict_name[first] = []
        dict_name[first].append(name)
        dict_name[first].sort()
    return dict_name
