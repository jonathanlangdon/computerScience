# get how many names are in database

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename

print(len(names_file.readlines()))
names_file.close()
