# return a dictionary of word lengths from a string


def word_lengths(text):
    puncts = [".", ",", "?", "!", "'"]
    for punct in puncts:
        text = text.replace(punct, "")
    words = text.lower().split(" ")
    word_dict = {}
    for word in words:
        word_dict[word] = len(word)
    return word_dict
