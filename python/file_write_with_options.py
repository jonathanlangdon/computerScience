# write to a file based on options given as arguments


def write_weird_file(filename, alist, mode="w", sort_first=False, reverse_first=False):
    if sort_first:
        alist.sort()
    if reverse_first:
        alist.reverse()
    open_file = open(filename, mode)
    for item in alist:
        print(item, file=open_file)
    open_file.close()
