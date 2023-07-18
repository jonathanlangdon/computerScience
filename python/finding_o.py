# find location of the "o" in a word


for word in words:
    try:
        print(word.index("o"))
    except:
        print("Not found")
