# Diamond Cuts

cut = "Emerald"
clarity = "VVS"
color = "Z"
carat = 1.1
budget = 500
preferred_cuts = ["Emerald", "Cushion", "Princess", "Oval"]

color_score = 100 - (ord(color) - ord("D")) * 2

clarity_score = ["I", "SI", "VS", "VVS", "IF", "F"]

final_cost = color_score * 2 ** clarity_score.index(clarity) * carat


def reaction():
    if final_cost < budget and cut in preferred_cuts:
        return "I'll take it!"
    else:
        return "No thanks"


print(reaction())

"""
use of the ord() method to find distances between characters
"""
