# do a linear search to find matches in a list


def search_for_string(string_list, the_string):
    index_list = []
    for i in range(len(string_list)):
        if string_list[i] == the_string:
            index_list.append(i)
    return index_list


# If your function works correctly, this will originally
# print: [1, 4, 5]
sample_list = [
    "artichoke",
    "turnip",
    "tomato",
    "potato",
    "turnip",
    "turnip",
    "artichoke",
]
print(search_for_string(sample_list, "turnip"))

sample_list2 = [1, 13, 24, 59, 24, 13, 25]
print(search_for_string(sample_list2, 13))
