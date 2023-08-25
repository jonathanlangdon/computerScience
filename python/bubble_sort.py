# fixed a bubble sort function that sorts an array


def sort_with_bubbles(a_list):
    swap_occurred = True

    while swap_occurred:
        swap_occurred = False
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
                sort_with_bubbles(a_list)

    return a_list


print(sort_with_bubbles([5, 3, 1, 2, 4]))
