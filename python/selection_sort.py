# fix a selection sort function


def sort_with_select(a_list):
    for i in range(len(a_list)):
        minIndex = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[minIndex]:
                minIndex = j

        # Save the current minimum value since we're about
        # to delete it
        minValue = a_list[minIndex]

        # Delete the minimum value from its current index
        del a_list[minIndex]

        # Insert the minimum value at its new index
        a_list.insert(i, minValue)

    # Return the resultant list
    return a_list


print(sort_with_select([5, 3, 1, 2, 4]))
