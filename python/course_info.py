# take list of tuples and convert to dictionary


def course_info(students):
    stud_dict = {}
    stud_list = []
    total_age = 0
    for name, age in students:
        stud_list.append(name)
        total_age += age
    stud_dict["students"] = stud_list
    stud_dict["avg_age"] = total_age / len(students)
    return stud_dict
