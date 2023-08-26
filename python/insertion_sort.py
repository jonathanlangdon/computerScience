# creating my own insertion sort


def insertion(unsorted):
    sorted_list = []

    def insert(unsorted, sorted_list):
        if not unsorted:
            return sorted_list
        if sorted_list == []:
            sorted_list = [unsorted[0]]
            unsorted = unsorted[1:]
        first_unsorted = unsorted[0]
        index = len(sorted_list) - 1
        while index >= 0 and sorted_list[index] > first_unsorted:
            index -= 1
        sorted_list.insert(index + 1, first_unsorted)
        return insert(unsorted[1:], sorted_list)

    return insert(unsorted, sorted_list)


# The code below will test your function. If your function
# works, it will print: [1, 2, 3, 4, 5].
print(insertion([5, 3, 1, 2, 4]))
