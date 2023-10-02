# How many total births are covered by the names in the database?

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename

lines = names_file.readlines()
total_births = 0
for line in lines:
    line_list = line.split(",")
    total_births += int(line_list[1])
print(total_births)
names_file.close()
