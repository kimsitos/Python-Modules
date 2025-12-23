#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Checks if the plant conditions are valid.

    Raises a ValueError if the plant name, water level,
    or sunlight hours are not acceptable.
    """
    if not plant_name.strip():
        raise ValueError("Please, insert a valid name")
    if water_level < 1 or water_level > 10:
        raise ValueError("Please, insert a reasonable water level")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("The sunlight hours is not reasonable")
    return "All good, enjoy!"


def test_plant_checks():
    """
    Tests the plant health checks with valid and invalid values.
    """
    print("=== Valid plant ===")
    print(check_plant_health("cactus", 5, 7))

    print("\n=== Invalid plant ===")
    try:
        check_plant_health(" ", 5, 4)
    except ValueError as error:
        print("Caught error:", error)

    try:
        check_plant_health("rose", 0, 7)
    except ValueError as error:
        print("Caught error:", error)

    try:
        check_plant_health("violet", 6, 18)
    except ValueError as error:
        print("Caught error:", error)
