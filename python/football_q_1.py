# determine first game ever played (and return the opponent)


def first_opponent():
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    record_file = open("football_records.csv", "r")
    record_list = record_file.readlines()
    record_file.close()
    del record_list[0]
    record_list = [x.split(",") for x in record_list]
    oldest_date = [9999, 99, 99]
    oldest_opponent = ""
    for record in record_list:
        cur_date = [int(num) for num in record[0].split("-")]
        if cur_date < oldest_date:
            oldest_date = cur_date
            oldest_opponent = record[1]
    return oldest_opponent


print(first_opponent())
