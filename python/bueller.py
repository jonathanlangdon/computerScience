# return a list of present students - dictionary practice


def students_present(a_dict):
    present_list = []
    for name, value in a_dict.items():
        if value == "Here" or value == "Present":
            present_list.append(name)
    return present_list
