#


def load_file(filename):
    open_file = open(filename, "r")
    output = open_file.readline()
    open_file.close()
    if output.isdigit():
        return int(output)
    try:
        return float(output)
    except:
        return output
