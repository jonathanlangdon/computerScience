# return even index characters as uppercase


def mock(text):
    result = ""
    for i in range(0, len(text)):
        if i % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i]
    return result
