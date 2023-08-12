# Loop practice with lyrics of a song

lyrics = [
    "I wanna be your endgame",
    "I wanna be your first string",
    "I wanna be your A-Team",
    "I wanna be your endgame, endgame",
]
lines_of_sanity = 6

lines = 0
while lines < lines_of_sanity:
    for line in lyrics:
        print(line)
        lines += 1
print("MAKE IT STOP")
