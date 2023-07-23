# return a requested number of marks


def random_marks(int1, int2, int3):
    return int1 * "'" + int2 * '"' + int3 * ''''"'''


print(random_marks(3, 2, 3))
