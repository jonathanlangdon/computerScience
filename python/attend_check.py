# create a list of students who are absent


def attendance_check(roster, present):
    absent = []
    for student in roster:
        if student in present:
            continue
        else:
            absent.append(student)
    absent.sort()
    return absent
