# baseball team scores - loop

away_team = [1, 0, 0, 2, 0, 0, 0, 0, 1]
home_team = [0, 1, 0, 0, 0, 0, 2, 0]

away_score = 0
home_score = 0

for runs in away_team:
    away_score += runs

for runs in home_team:
    home_score += runs

print("Home team wins!" if home_score > away_score else "Away team wins!")

"""
this could have been done with sum(), but we're practicing loops
"""
