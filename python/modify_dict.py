# find keys in a dictionary, then delete those key-value-pairs


def modify_dict(adict):
    del_list = []
    for lastname in adict.keys():
        if lastname == lastname.lower():
            del_list.append(lastname)
    for name in del_list:
        del adict[name]
    return adict
