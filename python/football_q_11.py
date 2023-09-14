# determine total record of Georgia Tech in home games


def georgia_record():
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    record_file = open("football_records.csv", "r")
    record_list = record_file.readlines()
    record_file.close()
    del record_list[0]
    record_list = [x.split(",") for x in record_list]
    win_tally = 0
    loss_tally = 0
    tie_tally = 0
    for record in record_list:
        if record[2] == "Home":
            score_difference = int(record[3]) - int(record[4].strip())
            if score_difference > 0:
                win_tally += 1
            elif score_difference < 0:
                loss_tally += 1
            else:
                tie_tally += 1
    return f"{win_tally}-{loss_tally}-{tie_tally}"


print(georgia_record())
