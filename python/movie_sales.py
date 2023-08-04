# return name of movie with biggest sales


def find_max_sales(data_list):
    highest_item = ("", 0)
    for _, sales in data_list:
        if sales > highest_item[1]:
            highest_item = (_, sales)
    return highest_item[0]
