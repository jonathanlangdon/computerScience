# count the number of consonants or vowels


def count_letters(text, find_consonants):
    if find_consonants:
        count = 0
        for char in text:
            if char in "bcdfghjklmnpqrstvwxyz":
                count += 1
        return count
    else:
        count = 0
        for char in text:
            if char in "aeiou":
                count += 1
        return count
