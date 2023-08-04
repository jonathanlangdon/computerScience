# return total population density from a list of country data (dictionaries)


def population_density(countries):
    total_pop = 0
    total_area = 0
    for country in countries:
        name, population, area = country.values()
        total_pop += population
        total_area += area
    return total_pop / total_area
