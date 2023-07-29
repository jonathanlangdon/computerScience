# search every line of a file for "!"


def angry_file_finder(filename):
    result = True
    open_file = open(filename, "r")
    for line in open_file.readlines():
        if not "!" in line:
            result = False
            break
    open_file.close()
    return result
