# search for text in a saved file


def search_in_files(filename, search_for):
    indices = []
    open_file = open(filename, "r")
    for i, line in enumerate(open_file, 1):
        if search_for in line:
            indices.append(i)
    open_file.close()
    return indices
