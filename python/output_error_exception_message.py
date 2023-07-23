# output the exact error message caught by the exception


def get_integer(my_var):
    try:
        return int(my_var)
    except Exception as e:
        return str(e)
