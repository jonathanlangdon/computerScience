# create a list of students who are absent using a for loop


def attendance_check(roster, present):
    absent = []
    for student in roster:
        if student in present:
            continue
        else:
            absent.append(student)
    absent.sort()
    return absent
