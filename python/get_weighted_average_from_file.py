# get grades from file and run a weighted average


def get_grade(filename):
    open_file = open(filename, "r")
    overall_grade = 0
    for line in open_file:
        [num, name, grade, total, weight] = line.split()
        overall_grade += int(grade) / int(total) * float(weight) * 100
    open_file.close()
    return overall_grade
