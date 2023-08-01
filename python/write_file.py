# take data and write to a file


def write_file(filename, data):
    file_out = open(filename, "w")
    file_out.write(str(data))
    file_out.close()


""" using print fxn

def write_file(filename, data):
    file_out = open(filename, "w")
    print(str(data), file=file_out)
    file_out.close()

"""
