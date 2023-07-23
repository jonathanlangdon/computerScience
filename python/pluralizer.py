# return the correct plural of a word


def pluralize(num, single, plural):
    return str(num) + " " + (single if num == 1 else plural)
