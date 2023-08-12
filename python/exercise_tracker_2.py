# practice adding a custom method to a class


class ExerciseSession:
    def __init__(self, exercise, intensity, duration):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration

    def get_exercise(self):
        return self.exercise

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.duration

    def set_exercise(self, new_exercise):
        self.exercise = new_exercise

    def set_intensity(self, new_intensity):
        self.intensity = new_intensity

    def set_duration(self, new_duration):
        self.duration = new_duration

    def calories_burned(self):
        intensities = {"Low": 4, "Medium": 8, "High": 12}
        return self.duration * intensities[self.intensity]
