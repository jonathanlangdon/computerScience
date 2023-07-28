# determine rough location of substring


def string_finder(target, search):
    found = target.find(search)
    if found == -1:
        return "Not found"
    elif found == 0:
        return "Beginning"
    elif found == len(target) - len(search):
        return "End"
    else:
        return "Middle"
