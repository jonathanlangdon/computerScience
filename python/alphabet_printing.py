# give sequence of letters from a start to an end

start_character = "A"
end_character = "Z"

asc_start = ord(start_character)
asc_end = ord(end_character) + 1

for num in range(asc_start, asc_end):
    print(chr(num))
