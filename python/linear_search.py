# search for a matching word and return the index


def linear(a_list, a_string):
    for i in range(len(a_list)):
        if a_list[i] == a_string:
            return i
    return False


a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))
