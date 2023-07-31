# take input file and restructure names into an output file with comma


def name_refixer(file_out, file_in):
    open_fo = open(file_out, "w")
    open_fi = open(file_in, "r")
    for item in open_fi:
        if "," in item:
            print(item.strip(), file=open_fo)
        words = item.split()
        if "," not in item:
            print(f"{words[2]}, {words[0]} {words[1]}", file=open_fo)
    open_fo.close() and open_fi.close()
