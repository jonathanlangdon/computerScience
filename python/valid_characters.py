# check if a string contains any characters not in a list of valid characters


def is_valid(str, valid_char):
    for char in str:
        if char not in valid_char:
            return False
    return True
