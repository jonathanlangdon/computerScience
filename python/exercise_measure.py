# return average of just the exercise portion of heart beats


def average_heart_rate(beats_list):
    workout_beats = list(filter(lambda x: x >= 100, beats_list))
    return sum(workout_beats) // len(workout_beats)
