# calculate the average word length of a string


def word_count(str):
    return str.count(" ") + 1


def letter_count(str):
    count = 0
    for char in str:
        if char != " ":
            count += 1
    return count


def average_word_length(str):
    return letter_count(str) / word_count(str)
