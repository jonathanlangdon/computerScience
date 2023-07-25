# return even index characters to the opposite case


def mock(text):
    result = ""
    for i in range(0, len(text)):
        if i % 2 == 0:
            if ord(text[i]) > 96:
                result += text[i].upper()
            else:
                result += text[i].lower()
        else:
            result += text[i]
    return result
