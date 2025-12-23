#!/usr/bin/env python3

def water_plants(plant_list):

    """
    Waters a list of plants and handles invalid plant names.
    The watering system is always closed using finally.
    """

    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed succesfully")

    except TypeError:
        print("Error: invalid plant name")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():

    """
    Tests the watering system with valid and invalid data.
    """

    print("=== Valid plant ===")
    water_plants(["rose", "tulip", "sunflower"])

    print("\n=== Invalid plant ===")
    water_plants(["rose", 59, "tulip"])
