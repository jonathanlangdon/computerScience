story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

grades = {
    "story": {"A": 6, "B": 5, "C": 4, "D": 2, "F": 0},
    "text": {"A": 5, "B": 4, "C": 3, "D": 1, "F": 0},
    "role": {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0},
    "director": {"A": 3, "B": 2, "C": 1, "D": 0, "F": 0},
    "cast": {"A": 2, "B": 1, "C": 0, "D": 0, "F": 0},
}

overall_grade = (
    grades["story"][story]
    + grades["text"][text]
    + grades["role"][role]
    + grades["director"][director]
    + grades["cast"][cast]
)

print(overall_grade)


def grade_category(grade):
    if grade == 20:
        return "Perfect score"
    elif grade >= 17:
        return "Must do"
    elif grade >= 14:
        return "Seriously consider"
    elif grade >= 12:
        return "On the bubble"
    elif grade >= 0:
        return "Pass"
    else:
        return "Invalid entry"


print(grade_category(overall_grade))
