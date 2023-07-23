# calculate damage to a pokemon


def calculate_modifier(STAB, Type, Critical, Other, Random):
    Modifier = STAB * Type * Critical * Other * Random
    return Modifier


def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    Damage = (
        (2 * Level + 10) / 250 * Attack / Defense * Base + 2
    ) * calculate_modifier(STAB, Type, Critical, Other, Random)
    return Damage
