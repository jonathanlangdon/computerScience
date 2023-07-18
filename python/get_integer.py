# try to convert to integer, with a catch for exceptions


def get_integer(my_var):
    try:
        return int(my_var)
    except:
        return "Cannot convert!"
