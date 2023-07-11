# Tag renewal exercise

car_value = 10000
purchase_year = 2011
car_age = 12
driver_age = 67
electric = False
emissions_passed = False

age_cost = 0
if purchase_year < 2013:
    age_cost = 0.01 * car_value

renewal_cost = round(20 + age_cost + electric * 200)

if emissions_passed or electric or (driver_age >= 65 and car_age >= 10):
    print(f"Your renewal fee is ${renewal_cost}.")
else:
    print("You must pass an emissions test first.")
