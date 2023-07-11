# moon phases

phase = "Half"
distance = 2228000
date = 23
eclipse = False

result = "Moon"

if phase == "Full":
    if eclipse:
        result = "Blood " + result
    if date > 28:
        result = "Blue " + result
    if distance < 230000:
        result = "Super " + result
    if result == "Moon":
        result = "Full " + result

print(result)

"""
practice with conditional statements
"""
