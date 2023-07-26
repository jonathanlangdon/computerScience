# return name of movie with biggest sales


def find_max_sales(alist):
    high_tuple = ("A movie", 0)
    for tuple in alist:
        (movie, sales) = tuple
        if sales > high_tuple[1]:
            high_tuple = tuple
    return high_tuple[0]
