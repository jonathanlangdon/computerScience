# return all text after 2nd instance of a search item


def after_second(search_in, search_for):
    first_index = search_in.find(search_for)
    second_index = search_in.find(search_for, first_index + 1)
    return search_in[(second_index + len(search_for)) :]
