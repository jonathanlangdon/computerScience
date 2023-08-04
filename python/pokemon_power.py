# take list of dictionaries and convert to a summary dictionary


def total_stats(pokemons):
    new_dict = {}
    for pokemon in pokemons:
        name = pokemon["name"]
        del pokemon["name"]
        total = sum(pokemon.values())
        new_dict[name] = total
    return new_dict
