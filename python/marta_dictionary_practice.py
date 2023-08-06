# sorting data from Marta using dictionaries


def three_questions():
    marta_file = open("../resource/lib/public/marta_01-18-2016.csv", "r")
    stations = {}
    for line in marta_file:
        station = line.split(",")[3]
        if station not in stations:
            stations[station] = 0
        stations[station] += 1
        avg = sum(stations.values()) / len(stations)
    print(f"The average taps per station are {round(avg)}")
    closest = (0, 999999)
    for station in stations:
        if abs(stations[station] - avg) < abs(closest[1] - avg):
            closest = station, stations[station]
    print(f"the closest to avg is {closest}")
    sorted_station = sorted(stations.items(), key=lambda x: x[1])
    print(f"the least used station is {sorted_station[0]}")


three_questions()
