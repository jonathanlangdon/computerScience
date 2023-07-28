# convert char in a string to its ordinal numbers


def string_to_ordinals(text):
    result = ""
    for char in text:
        result += str(ord(char))
    return result
