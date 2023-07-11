# grading feedback

grade = 72
curve = 5

new_grade = grade + curve

if new_grade > 100:
    new_grade = 100

if new_grade >= 90:
    print(f"Congratulations! Your final grade is {new_grade}, an A.")
elif new_grade >= 80:
    print(f"Good job! Your final grade is {new_grade}, a B.")
elif new_grade >= 70:
    print(f"Not bad! Your final grade is {new_grade}, a C.")
elif new_grade >= 60:
    print(f"You passed! Your final grade is {new_grade}, a D.")
else:
    print(f"It's just one grade. Your final grade is {new_grade}, an F.")

"""
practice with conditionals
"""
