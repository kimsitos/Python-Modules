import alchemy.elements as element


def healing_potion() -> str:
    return (f"Healing potion brewed with {element.create_fire()} "
            f"and {element.create_water()}")


def strength_potion() -> str:
    return (f"Strenght potion brewed with {element.create_earth()} "
            f"and {element.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {element.create_air()} "
            f"and {element.create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {element.create_earth()}"
            f", {element.create_fire()}, {element.create_water()} and "
            f"{element.create_air()}")
