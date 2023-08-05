#


def reader(filename):
    open_file = open(filename, "r")
    grade_dict = {}
    for line in open_file:
        num, name, grade, total, wght = line.split(" ")
        grade_dict[name] = {
            "number": int(num),
            "grade": int(grade),
            "total": int(total),
            "weight": float(wght),
        }
    open_file.close()
    return grade_dict
