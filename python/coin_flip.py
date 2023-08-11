# count heads and tails and determine winner

flips = "HHTHHHTTHHTHTHHHTHH"

head = flips.count("H")
tail = flips.count("T")
result = ""

if head > tail:
    result = "Heads wins."
elif tail > head:
    result = "Tails wins."
else:
    result = "It's a tie."

print(f"{head} heads, {tail} tails. {result}")
