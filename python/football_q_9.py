# determine a team that scored 0 against G-Tech


def georgia_record():
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    record_file = open("football_records.csv", "r")
    record_list = record_file.readlines()
    record_file.close()
    del record_list[0]
    record_list = [x.split(",") for x in record_list]
    opponent_dict = {}
    for record in record_list:
        if record[1] not in opponent_dict.keys():
            opponent_dict[record[1]] = 0
        opponent_dict[record[1]] += int(record[4])

    return min(opponent_dict, key=opponent_dict.get)


print(georgia_record())
