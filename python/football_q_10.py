# determine highest scoring differential record (if team played 5+ games)


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
            opponent_dict[record[1]] = [0, 0]  # [# games, pt difference]
        opponent_dict[record[1]][0] += 1
        opponent_dict[record[1]][1] += int(record[3]) - int(record[4])
    common_opponent_dict = {}  # value = average pt differential
    for opponent, [games, differential] in opponent_dict.items():
        if games < 5:
            continue
        common_opponent_dict[opponent] = differential / games

    return max(common_opponent_dict, key=common_opponent_dict.get)


print(georgia_record())
