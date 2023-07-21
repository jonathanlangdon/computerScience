# print characters one at a time of items in a list

given_items = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

for item in given_items:
    try:
        for char in item:
            print(char)
    except:
        print("Not iterable")
