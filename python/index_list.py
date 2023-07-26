# list all of the indices of a search item found in a list


def inside_search(alist, search_for):
    index_list = []
    for item in alist:
        if search_for in item:
            index_list.append(alist.index(item))
    return index_list
