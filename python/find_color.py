# interpret rgb codes


def find_color(rgb):
    rgb_digits = rgb[4:-1].split(", ")
    red = int(rgb_digits[0])
    green = int(rgb_digits[1])
    blue = int(rgb_digits[2])
    if red > green and red > blue:
        return "red"
    elif green > red and green > blue:
        return "green"
    elif blue > red and blue > green:
        return "blue"
    elif red == blue and red == green:
        return "gray"
    elif red == green:
        return "yellow"
    elif red == blue:
        return "purple"
    elif green == blue:
        return "teal"
    else:
        return "invalid color"
