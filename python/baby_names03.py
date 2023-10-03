# How many different boys' names are there that begin with the letter Z?

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename
# sample line: Isabella,42567,Girl

lines = names_file.readlines()
total_z_boy_names = 0
for line in lines:
    line_list = line.strip().split(",")
    if line_list[0][0] == "Z" and line_list[2] == "Boy":
        total_z_boy_names += 1
print(total_z_boy_names)
names_file.close()
