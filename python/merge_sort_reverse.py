# take merge sort and reverse it


def sort_with_merge(lst):
    if len(lst) <= 1:
        return lst

    midpoint = len(lst) // 2
    left = sort_with_merge(lst[:midpoint])
    right = sort_with_merge(lst[midpoint:])

    newlist = []
    while len(left) and len(right) > 0:
        if left[0] < right[0]:
            newlist.append(right[0])
            del right[0]
        else:
            newlist.append(left[0])
            del left[0]

    newlist.extend(left)
    newlist.extend(right)

    return newlist


# The code below will test your function. If it works, this
# will print [5, 3, 1, -1, -3, -5].
print(sort_with_merge([1, 3, -1, -3, -5, 5]))
