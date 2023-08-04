# translate words to french based on dictionary

french_dict = {
    "me": "moi",
    "hello": "bonjour",
    "goodbye": "au revoir",
    "cat": "chat",
    "dog": "chien",
    "and": "et",
}


def french2eng(sentence):
    words = sentence.lower().split()
    for i in range(0, len(words)):
        if words[i] in french_dict:
            words[i] = french_dict[words[i]]
    return " ".join(words)
