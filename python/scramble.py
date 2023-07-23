# slicing to swap the two halves of a string


def scramble(text):
    return text[len(text) // 2 :] + text[: len(text) // 2]
