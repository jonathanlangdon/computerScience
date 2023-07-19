#

score = 500
difficulty_bonus = 1.2
perfect_run = True

performer_bonus = 0
if score > 200:
    performer_bonus = 200
if perfect_run:
    score *= 2
final_score = score * difficulty_bonus + performer_bonus

print(f"Your final score is: {int(final_score)}")
