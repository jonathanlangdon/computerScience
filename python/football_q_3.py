# determine how many points Auburn scored against Goergia Tech


def first_opponent():
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    record_file = open("football_records.csv", "r")
    record_list = record_file.readlines()
    record_file.close()
    del record_list[0]
    record_list = [x.split(",") for x in record_list]
    total_auburn = 0
    for record in record_list:
        if record[1] == "Auburn":
            total_auburn += int(record[4])
    return total_auburn


print(first_opponent())
