mystery_list = ["John Smith", "Thirty One", "Michigan State"]

count = 0
for string in mystery_list:
    for letter in string:
        if letter.lower() == "t":
            count += 1

print(count)
