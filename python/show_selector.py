# a function that helps determine what you should watch


def select_a_show(min):
    if min <= 0:
        return "You're late!"
    elif min <= 10:
        return "Leave now, be early!"
    elif min <= 45:
        return "Watch a comedy!"
    elif min <= 100:
        return "Watch a drama!"
    else:
        return "Watch a movie!"
