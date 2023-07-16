# count the measures and beats, but the first beat will match the current measure

beats_per_measure = 3
measures = 6

for measure in range(1, measures + 1):
    print(measure)
    for beat in range(2, beats_per_measure + 1):
        print(beat)
