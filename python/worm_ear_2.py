# print lines of song until reach sanity level

lyrics = [
    "I wanna be your endgame",
    "I wanna be your first string",
    "I wanna be your A-Team",
    "I wanna be your endgame, endgame",
]
lines_of_sanity = 3

lines = 0
while lines < lines_of_sanity:
    for line in lyrics:
        print(line)
        lines += 1
        if lines == lines_of_sanity:
            break
print("MAKE IT STOP")
