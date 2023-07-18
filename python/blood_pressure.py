# given blood pressure, return whether it is high or not


def check_blood_pressure(systolic, diastolic):
    if systolic < 90 and diastolic < 60:
        return "Low"
    elif systolic < 120 and diastolic < 80:
        return "Ideal"
    elif systolic < 140 and diastolic < 90:
        return "Pre-high"
    else:
        return "High"
