# return 3rd character of a string


def third_character(text):
    if len(text) < 3:
        return "Too short"
    else:
        return text[2]
