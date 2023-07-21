# find and return text within parentheses


def in_parentheses(text):
    start = text.find("(") + 1
    end = text.find(")")
    if start == 0 or end == -1:
        return ""
    else:
        return text[start:end]
