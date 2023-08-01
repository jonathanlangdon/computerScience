# count the number of words with error handling


def word_count(my_string):
    try:
        return my_string.count(" ") + 1
    except:
        return "Not a string"
