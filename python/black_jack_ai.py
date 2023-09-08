# a programmed black jack dealer


def next_move(cards):
    total = 0
    num_aces = 0
    for card in cards:
        if card == "0":
            total += 10
        elif card.isdigit():
            total += int(card)
        elif card == "A":
            num_aces += 1
        else:
            total += 10
    for ace in range(num_aces):
        score11 = total + 11
        if score11 > 16 and score11 < 22:
            total += 11
        else:
            total += 1
    if total < 17:
        return "Hit"
    elif total >= 17 and total < 22:
        return "Stay"
    else:
        return "Bust"


print(next_move("A3"))  # Hit
print(next_move("A39"))  # Hit
print(next_move("A397"))  # Stay
print(next_move("A397K"))  # Bust
print(next_move("7A0"))  # Stay
print(next_move("J30"))  # Bust
