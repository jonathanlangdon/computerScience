# imitate the .split() method


def string_splitter(a_string):
    new_list = []
    spaces_index = [-1]
    for i in range(0, len(a_string)):
        if a_string[i] == " ":
            spaces_index.append(i)
    spaces_index.append(len(a_string))
    for i in range(0, len(spaces_index) - 1):
        new_list.append(a_string[spaces_index[i] + 1 : spaces_index[i + 1]])
    return new_list
