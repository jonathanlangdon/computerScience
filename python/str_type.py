# determine what type of string is inputed


def string_type(text):
    if text == "":
        return "empty"
    elif len(text) == 1:
        return "character"
    elif text.count("\n") > 0:
        return "page"
    elif text.count(" ") == 0:
        return "word"
    per_count = text.count(".")
    if per_count < 2:
        return "sentence"
    elif per_count > 1:
        return "paragraph"
