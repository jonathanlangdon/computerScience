# a fxn that calculate how many spaces to align right text


def align_right(a_string, string_length):
    num_spaces = string_length - len(a_string)
    return f"{num_spaces * ' '}{a_string}"
