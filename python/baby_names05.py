# How many total babies were given names that both start and end with vowels (A, E, I, O, or U)

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename
# sample line: Isabella,42567,Girl//newline

lines = names_file.readlines()
total_vowel_babies = 0
vowels = ["a", "e", "i", "o", "u"]
for line in lines:
    [name, name_count_string, gender] = line.strip().lower().split(",")
    if name[0] in vowels and name[-1] in vowels:
        total_vowel_babies += int(name_count_string)
print(total_vowel_babies)
names_file.close()
