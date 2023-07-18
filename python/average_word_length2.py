# calculate the average word length with error handling
import re


def word_count(my_string):
    return len(my_string.split())


def letter_count(my_string):
    return len(re.findall(r"[a-zA-Z]", my_string))


def average_word_length(my_string):
    try:
        count = letter_count(my_string)
    except:
        return "Not a string"
    if count == 0:
        return "No words"
    return count / word_count(my_string)


print(average_word_length(True))
