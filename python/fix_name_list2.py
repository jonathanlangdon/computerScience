# fix formatting of names submitted


def name_refixer(the_list):
    new_list = []
    for item in the_list:
        if "," in item:
            new_list.append(item)
        words = item.split()
        if "," not in item:
            new_list.append(f"{words[2]}, {words[0]} {words[1]}")
    return new_list
