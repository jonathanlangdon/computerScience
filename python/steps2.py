# print steps in a certain order


def steps(num):
    text = ""
    for i in range(1, num + 1):
        text += "\t" * (i - 1) + str(111 * i) + "\n"
    return text
