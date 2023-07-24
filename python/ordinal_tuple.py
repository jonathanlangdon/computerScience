# return a 3-tuple of character info about a single char


def character_info(char):
    char_type = ""
    if ord(char) in range(48, 58):
        char_type = "number"
    elif ord(char) in range(65, 91) or ord(char) in range(97, 123):
        char_type = "letter"
    else:
        char_type = "punctuation"
    return char, ord(char), char_type
