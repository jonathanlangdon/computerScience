# identify the type of input from a user


def input_type(text):
    if text.find(".") == -1:
        try:
            int(text)
            return "integer"
        except:
            pass
    try:
        float(text)
        return "float"
    except:
        if text == "True" or text == "False":
            return "boolean"
        else:
            return "string"
