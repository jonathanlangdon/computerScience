# an elaborate way to find a substring


def fancy_find(search_within, search_for):
    if search_for in search_within:
        return f"{search_for} found at index {search_within.find(search_for)}!"
    else:
        return f"{search_for} was not found within {search_within}!"
