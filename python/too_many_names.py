# make a dictionary count of number of occurances of names


def name_counts(names):
    count_name = {}
    for name in names:
        (first, last) = name.split()
        if first not in count_name:
            count_name[first] = 0
        count_name[first] += 1
    return count_name
