# take 2 files and find if any sequence of 5 words are the same


def check_plagiarism(file1, file2):
    open_file1 = open(file1, "r")
    open_file2 = open(file2, "r")
    list1 = open_file1.readline().strip().lower().split(" ")
    list2 = open_file2.readline().strip().lower().split(" ")
    open_file1.close()
    open_file2.close()
    set1 = set(list1)
    set2 = set(list2)
    list_of_repeats = []
    is_cheater = False

    def check_sequence(index1, index2):
        if list1[index1] != list2[index2]:
            return 0
        elif len(list1) - 1 == index1 or len(list2) - 1 == index2:
            return 0
        else:
            return 1 + check_sequence(index1 + 1, index2 + 1)

    for word in set1:
        if word in set2:
            indices1 = [index for (index, item) in enumerate(list1) if item == word]
            indices2 = [index for (index, item) in enumerate(list2) if item == word]
            for index1 in indices1:
                for index2 in indices2:
                    repeat_length = check_sequence(index1, index2)
                    if repeat_length >= 5:
                        is_cheater = True
                        list_of_repeats.append(
                            (
                                repeat_length,
                                " ".join(list1[index1 : index1 + repeat_length]),
                            )
                        )

    if is_cheater:
        return max(list_of_repeats, key=lambda x: x[0])[1]
    else:
        return False


print(check_plagiarism("file_1.txt", "file_2.txt"))
# if i go crazy then
print(check_plagiarism("file_1.txt", "file_3.txt"))
# i left my body lying somewhere in the sands of time
print(check_plagiarism("file_2.txt", "file_3.txt"))
# False
