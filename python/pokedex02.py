# What is the most common type? Include both Type1 and Type2 in your count.

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
        self.legendary = legendary.capitalize()
        self.mega = mega.capitalize()

    def __str__(self):
        return f"Pokemon{self.num}: {self.name}"


pokemon_list = []
for line in pokedex:
    stats = line.strip().split(",")
    pokemon_list.append(Pokemon(*stats))
pokedex.close()

type_dict = {}

for pokemon in pokemon_list:
    count = type_dict.setdefault(pokemon.type1, 0)
    type_dict[pokemon.type1] = count + 1

    count = type_dict.setdefault(pokemon.type2, 0)
    type_dict[pokemon.type2] = count + 1

del type_dict[""]

print(type_dict)
print("the most common type is", max(type_dict, key=type_dict.get))

# line 1: 'Number,Name,Type1,Type2,HP,Attack,Defense,SpecialAtk,SpecialDef,Speed,Generation,Legendary,Mega\n'
# line 2: '2,Bulbasaur,Grass,Poison,45,49,49,65,65,45,1,FALSE,FALSE\n'
