# take input file and restructure names into an output file


def name_fixer(file_out, file_in):
    open_fo = open(file_out, "w")
    open_fi = open(file_in, "r")
    for item in open_fi:
        if "," not in item:
            print(item.strip(), file=open_fo)
        words = item.split()
        if "," in words[0]:
            words[0] = words[0].replace(",", "")
            print(f"{words[1]} {words[2]} {words[0]}", file=open_fo)
    open_fo.close() and open_fi.close()
