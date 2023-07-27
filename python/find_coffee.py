# determine if "coffee" is anywhere in a file


def find_coffee(filename):
    result = False
    open_file = open(filename, "r")
    if "coffee" in open_file.read():
        result = True
    open_file.close()
    return result
