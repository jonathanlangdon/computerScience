# Among all 7 Pokemon generations, which generation had the highest average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

pokedex = open("pokedex.csv", "r")
# above is for testing, but use actual data source

header = next(pokedex)


class Pokemon:
    def __init__(
        self,
        num,
        name,
        type1,
        type2,
        hp,
        attack,
        defense,
        special_atk,
        special_def,
        speed,
        generation,
        legendary,
        mega,
    ):
        self.num = int(num)
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.special_atk = int(special_atk)
        self.special_def = int(special_def)
        self.speed = int(speed)
        self.generation = int(generation)
        self.legendary = legendary == "TRUE"
        self.mega = mega == "TRUE"

    def __str__(self):
        return f"Pokemon{self.num}: {self.name}"


pokemon_list = []
for line in pokedex:
    stats = line.strip().split(",")
    pokemon_list.append(Pokemon(*stats))
pokedex.close()

mega_dict = {"sum": 0, "count": 0}
nonmega_dict = {"sum": 0, "count": 0}
mega_numbers = []
nonmega_dict_stats = {}


def make_mega_list():
    for pokemon in pokemon_list:
        if pokemon.mega:
            mega_numbers.append(pokemon.num)


def sum_stats(pokemon):
    return sum(
        [
            pokemon.hp,
            pokemon.attack,
            pokemon.defense,
            pokemon.special_atk,
            pokemon.special_def,
            pokemon.speed,
        ]
    )


def make_nonmega_dict_stats():
    for pokemon in pokemon_list:
        if pokemon.num in mega_numbers and not pokemon.mega:
            if pokemon.num not in nonmega_dict_stats:
                nonmega_dict_stats[pokemon.num] = sum_stats(pokemon)


def make_dictionaries_of_stat_totals():
    for pokemon in pokemon_list:
        if pokemon.num in mega_numbers and pokemon.mega:
            stats_sum = sum_stats(pokemon)
            mega_dict["sum"] += stats_sum
            mega_dict["count"] += 1
            nonmega_dict["sum"] += nonmega_dict_stats[pokemon.num]
            nonmega_dict["count"] += 1


def find_average(dict):
    return dict["sum"] / dict["count"]


make_mega_list()
make_nonmega_dict_stats()
make_dictionaries_of_stat_totals()
avg_mega = find_average(mega_dict)
avg_nonmega = find_average(nonmega_dict)
difference = round(avg_mega - avg_nonmega)

print("the Mega pokemon are on average", difference, "higher than their counterparts")

# line 1: 'Number,Name,Type1,Type2,HP,Attack,Defense,SpecialAtk,SpecialDef,Speed,Generation,Legendary,Mega\n'
# line 2: '2,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,FALSE,FALSE\n'
