# avergae all the lines of a file


def average_file(filename):
    opened_file = open(filename, "r")
    numbers = []
    for line in opened_file.readlines():
        try:
            numbers.append(int(line))
        except:
            opened_file.close()
            return "Error reading file!"
    opened_file.close()
    return sum(numbers) / len(numbers)
