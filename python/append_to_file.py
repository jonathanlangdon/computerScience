# append data to end of file


def append_to_file(filename, data):
    file_out = open(filename, "a")
    print(str(data), file=file_out)
    file_out.close()
