# print how many times a character is in a string

mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

count = 0
for char in mystery_string:
    if char == mystery_character:
        count += 1

print(count)
