# what would be the most common name in the 2010s regardless of gender?

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename
# sample line: Isabella,42567,Girl//newline

lines = names_file.readlines()
smallest_difference_unigender_name = ("noName", 99999999)
list_of_all_names = []
for line in lines:
    [name, name_count_string, gender] = line.strip().lower().split(",")
    list_of_all_names.append((name, int(name_count_string)))
sorted_names = sorted(list_of_all_names, key=lambda x: x[0])
for index, name_tuple in enumerate(sorted_names):
    if index == 0:
        continue
    [cur_name, cur_count] = name_tuple
    if cur_name == sorted_names[index - 1][0]:
        cur_difference = abs(cur_count - sorted_names[index - 1][1])
        if cur_difference < smallest_difference_unigender_name[1]:
            smallest_difference_unigender_name = (cur_name, cur_difference)
print(smallest_difference_unigender_name)
names_file.close()
