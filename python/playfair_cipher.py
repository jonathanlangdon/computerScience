# Create encryption/decryption function for a playfair cipher

import re

CIPHER = (
    ("D", "A", "V", "I", "O"),
    ("Y", "N", "E", "R", "B"),
    ("C", "F", "G", "H", "K"),
    ("L", "M", "P", "Q", "S"),
    ("T", "U", "W", "X", "Z"),
)


def correctly_format(a_string):
    to_encrypt = a_string.upper().replace("J", "I")
    to_encrypt = re.sub(r"\W", "", to_encrypt)
    if len(to_encrypt) % 2 != 0:
        to_encrypt += "X"
    return to_encrypt


def split_into_pair_list(a_string):
    two_char = ""
    pair_list = []
    for char in a_string:
        two_char += char
        if len(two_char) == 2:
            if two_char[1] == two_char[0]:
                two_char = two_char[0] + "X"
            pair_list.append(two_char)
            two_char = ""
    return pair_list


def cipher_index(letter):
    for row_index, row in enumerate(CIPHER):
        if letter in row:
            return (row_index, row.index(letter))


def locate_letters(pair_list):
    letter_locations = []
    for pairs in pair_list:
        letter1 = pairs[0]
        letter2 = pairs[1]
        letter_locations.append((cipher_index(letter1), cipher_index(letter2)))
    return letter_locations


def increase_by_one(num):
    if num == 4:
        return 0
    else:
        return num + 1


def decrease_by_one(num):
    if num == 0:
        return 4
    else:
        return num - 1


def return_crypted_pair(pair_location, direction):
    (location1, location2) = pair_location
    (loc1row, loc1col) = location1
    (loc2row, loc2col) = location2
    # vertical match
    if loc1col == loc2col:
        if direction == "encrypt":
            loc1row = increase_by_one(loc1row)
            loc2row = increase_by_one(loc2row)
        if direction == "decrypt":
            loc1row = decrease_by_one(loc1row)
            loc2row = decrease_by_one(loc2row)
        return CIPHER[loc1row][loc1col] + CIPHER[loc2row][loc2col]
    # horizontal match
    if loc1row == loc2row:
        if direction == "encrypt":
            loc1col = increase_by_one(loc1col)
            loc2col = increase_by_one(loc2col)
        if direction == "decrypt":
            loc1col = decrease_by_one(loc1col)
            loc2col = decrease_by_one(loc2col)
        return CIPHER[loc1row][loc1col] + CIPHER[loc2row][loc2col]
    # rectangle match
    else:
        return CIPHER[loc1row][loc2col] + CIPHER[loc2row][loc1col]


def found_location_pairs(f_string):
    pair_list = split_into_pair_list(f_string)
    return locate_letters(pair_list)


def encrypt(a_string):
    formatted_string = correctly_format(a_string)
    encrypted_string = ""
    for pair in found_location_pairs(formatted_string):
        encrypted_string += return_crypted_pair(pair, "encrypt")
    return encrypted_string


def decrypt(f_string):
    decrypted_string = ""
    for pair in found_location_pairs(f_string):
        decrypted_string += return_crypted_pair(pair, "decrypt")
    return decrypted_string


# print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))
