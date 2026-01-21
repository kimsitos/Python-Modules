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

    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["rose", "tulip", "sunflower"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["rose", 59, "tulip"])
    print("\nCleanup always happens, even with errors!")


test_watering_system()
