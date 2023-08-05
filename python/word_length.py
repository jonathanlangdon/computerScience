# create dictionary of words organized by word length


def length_words(text):
    puncts = [".", ",", "?", "!", "'"]
    for punct in puncts:
        text = text.replace(punct, "")
    words = text.lower().split(" ")
    word_dict = {}
    for word in words:
        if len(word) not in word_dict:
            word_dict[len(word)] = []
        word_dict[len(word)].append(word)
    return word_dict
