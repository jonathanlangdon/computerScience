mystery_string = "Would you like to go outside?"
mystery_character = "o"

count = 0
for letter in mystery_string:
    if letter == mystery_character:
        count += 1

print(count)
