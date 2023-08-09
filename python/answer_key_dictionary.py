# check student test vs answer key (both are dictionaries)


def calculate_score(student_test, answer_key):
    if len(student_test) != len(answer_key):
        return -1
    score = 0
    i = 1
    while i <= len(student_test):
        if student_test[i] == answer_key[i]:
            score += 1
        i += 1
    return score
