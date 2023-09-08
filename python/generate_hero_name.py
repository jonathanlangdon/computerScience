# take a name input and output a hero name from a file


def generate_name(hero_file, user_name):
    name_arr = user_name.split()
    first_initial = ord(name_arr[0][0]) - 65
    last_initial = ord(name_arr[1][0]) - 39
    with open(hero_file, "r") as file:
        heroes = file.readlines()
        return heroes[first_initial].strip() + " " + heroes[last_initial].strip()


print(generate_name("heronames.txt", "Addison Zook"))
print(generate_name("heronames.txt", "Uma Irwin"))
print(generate_name("heronames.txt", "David Joyner"))
