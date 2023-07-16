# determine how many times the word cat appears

mystery_string = "catcatcatcatcat!!"

match_count = 0
count = 0

for char in mystery_string:
    if char == "cat"[match_count]:
        match_count += 1
    else:
        match_count = 0
    if match_count == 3:
        count += 1
        match_count = 0

print(count)
