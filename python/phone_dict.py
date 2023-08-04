# create a new dictionrary from two lists


def phonebook(names, numbers):
    new_dict = {}
    for i in range(0, len(names)):
        new_dict[names[i]] = numbers[i]
    return new_dict
