# In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.

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

legendary_dict = {}

for pokemon in pokemon_list:
    if pokemon.legendary:
        stats = [
            pokemon.hp,
            pokemon.attack,
            pokemon.defense,
            pokemon.special_atk,
            pokemon.special_def,
            pokemon.speed,
        ]
        stats_sum = sum(stats)
        legendary_dict[pokemon.name] = stats_sum

print(min(legendary_dict, key=legendary_dict.get))

# line 1: 'Number,Name,Type1,Type2,HP,Attack,Defense,SpecialAtk,SpecialDef,Speed,Generation,Legendary,Mega\n'
# line 2: '2,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,FALSE,FALSE\n'
