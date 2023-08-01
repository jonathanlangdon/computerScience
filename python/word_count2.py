# count the number of words with error handling


def word_count(my_string):
    try:
        return len(my_string.split())
    except:
        return "Not a string"
