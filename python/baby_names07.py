# What letter is the most common first letter of a baby's name (in terms of number of babies with names starting with that letter, not number of names)?

names_file = open("baby_names.csv", "r")
# in actual database, use the actual filename
# sample line: Isabella,42567,Girl//newline

lines = names_file.readlines()
least_common_first_letter = ("$", 0)
letters = "qwertyuiopasdfghjklzxcvbnm"
for letter in letters:
    current_letter_count = 0
    for line in lines:
        [name, name_count_string, gender] = line.strip().lower().split(",")
        if name[0] == letter:
            current_letter_count += int(name_count_string)
    if current_letter_count > least_common_first_letter[1]:
        least_common_first_letter = (letter, current_letter_count)

print(least_common_first_letter)
names_file.close()
