# practice creating methods(getters, setters) in a class


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
