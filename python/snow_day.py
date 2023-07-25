# function that determines of school is closed on weather


def snowed_in(temperature, weather, is_celsius=True):
    return temperature < (0 if is_celsius else 32) or weather == "snowy"
