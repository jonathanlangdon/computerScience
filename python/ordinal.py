# test if a character is valid for a password (keys on keyboard)


def valid_char(char):
    return ord(char) > 32 and ord(char) < 127
