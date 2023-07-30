# determine if a list has 3 sevens in a row in it


def lucky_sevens(alist):
    count7 = 0
    for num in alist:
        if num == 7:
            count7 += 1
        else:
            count7 = 0
        if count7 == 3:
            return True
    return False
