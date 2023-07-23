# convert a string of an octal (base 8) to decimal (base 10)


def octal_to_decimal(text):
    result = 0
    result += int(text[0]) * 512
    result += int(text[1]) * 64
    result += int(text[2]) * 8
    result += int(text[3]) * 1
    return result
