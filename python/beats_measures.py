# practice making a nested loop - mimicing a conducting counting the beat in a song

beats_per_measure = 2
measures = 3

for measure in range(1, measures + 1):
    for beat in range(1, beats_per_measure + 1):
        print(beat)
