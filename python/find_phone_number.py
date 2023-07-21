# find 10 digit phone number in a string


def find_phone_number(text):
    split_arr = text.split(" ")
    for item in split_arr:
        if len(item) == 10:
            try:
                int(item)
                return item
            except:
                pass
