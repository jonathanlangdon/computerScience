# return whether a string has a vowel in it


def has_a_vowel(a_str):
    print("Starting...")
    for letter in a_str:
        print("Checking", letter)
        if letter in "aeiou":
            print(letter, "is a vowel, returning True")
            return True
    print("Done!")
    return False


print(has_a_vowel("jtwrj wrjl!"))
