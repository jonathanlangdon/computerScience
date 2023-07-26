# fix names submitted


def name_fixer(the_list):
    new_list = []
    for item in the_list:
        if "," not in item:
            new_list.append(item)
        words = item.split()
        if "," in words[0]:
            words[0] = words[0].replace(",", "")
            new_list.append(f"{words[1]} {words[2]} {words[0]}")
    return new_list
