# determine if a NBA team is a contender for a championship


def is_a_contender(team, wins, losses):
    if wins >= 40 and losses < 20:
        return f"The {team} are a contender!"
    elif wins < 40 and losses >= 20:
        return f"The {team} are not a contender!"
    else:
        return f"The {team} might be a contender!"
