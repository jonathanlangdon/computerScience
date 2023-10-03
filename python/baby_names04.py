# What is the most common girl's name that begins with the letter Q?

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename
# sample line: Isabella,42567,Girl//newline

lines = names_file.readlines()
commonest_Q_girl_name = ("no_name", 0)
for line in lines:
    [name, name_count_string, gender] = line.strip().split(",")
    if name[0] == "Q" and gender == "Girl":
        name_count = int(name_count_string)
        if name_count > commonest_Q_girl_name[1]:
            commonest_Q_girl_name = (name, name_count)
print(commonest_Q_girl_name[0])
names_file.close()
