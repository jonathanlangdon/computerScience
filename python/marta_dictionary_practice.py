# sorting data from Marta using dictionaries


def three_questions():
    marta_file = open("../resource/lib/public/marta_01-18-2016.csv", "r")
    stations = {}
    for line in marta_file:
        station = line.split(",")[3]
        if station not in stations:
            stations[station] = 0
        stations[station] += 1
    print(f"The stations are {stations}")
