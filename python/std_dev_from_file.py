# calculate standard deviation of a list of integers in a file

from math import sqrt


def st_dev(filename):
    file = open(filename, "r")
    int_data = []
    for line in file:
        int_data.append(int(line))
    file.close()
    mean = sum(int_data) / len(int_data)
    dif_data = []
    for item in int_data:
        dif_data.append((item - mean) ** 2)
    return (sum(dif_data) / len(dif_data)) ** 0.5
