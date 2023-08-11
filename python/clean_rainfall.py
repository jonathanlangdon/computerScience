# cleanup data of rainfall


def clean_data(rainfall):
    del_list = []
    for loc, rain in rainfall.items():
        try:
            if rain < 0 or rain > 100:
                del_list.append(loc)
                print(del_list)
        except:
            pass
        if type(rain) == int or type(rain) == float:
            continue
        else:
            del_list.append(loc)
            print(del_list)
    for data in del_list:
        del rainfall[data]
    return rainfall
