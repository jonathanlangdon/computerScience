# return number of answers match key


def grade_scantron(answers, key):
    if len(answers) != len(key):
        return -1
    correct = 0
    for i in range(0, len(key)):
        if key[i] == answers[i]:
            correct += 1
    return correct
