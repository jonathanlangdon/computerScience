# return first 3 items in a tuple reversed


def unpack_and_reverse(tuple1):
    one, two, three, *_ = tuple1
    return three, two, one
