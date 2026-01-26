#!/usr/bin/env python3

# Errors
class GardenError(Exception):
    """Base error for garden problems."""
    def __init__(self, message="Something went wrong in the garden"):
        super().__init__(message)


class PlantError(GardenError):
    """Error related to plants."""
    def __init__(self, message="Something went wrong with the plants"):
        super().__init__(message)


class WaterError(GardenError):
    """Checks if the plant height is valid."""
    def __init__(self, message="Something went wrong with the Water"):
        super().__init__(message)


# GardenManager class
class GardenManager:
    """Manages a plant, its water, sunlight, and health."""
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name, water_level, sunlight_hours):
        """Initialize a plant and validate its parameters."""
        if not plant_name.strip():
            raise GardenError("Plant name empty")

        if water_level < 1 or water_level > 10:
            raise GardenError("Not reasonable water level. (min 1, max 10)")

        if sunlight_hours < 2 or sunlight_hours > 12:
            raise GardenError("The sunlight hours is not reasonable")

        self.plants.append({'name': plant_name,
                           'water_level': water_level,
                            'sunlight_hours': sunlight_hours})
        print(f"Added {plant_name} succesfully")

    def water_plant(self):
        """Water the plant, decrease water level, raise error if not enought"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant['water_level'] += 1
                print(f"Watering {plant['name']} - success")
        except Exception:
            raise WaterError(f"Not enough water for {plant['name']}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        """Check plant's health and raise error if conditions are invalid."""
        for plant in self.plants:
            if not plant['name']:
                raise PlantError("Not a good name for the plant")

            if plant['water_level'] < 1 or plant['water_level'] > 10:
                raise PlantError(f"{plant['water_level']} "
                                 "is not a good water level")

            if plant['sunlight_hours'] < 2 or plant['sunlight_hours'] > 12:
                raise PlantError(f"{plant['sunlight_hours']}h "
                                 "of sunlight is not good")
            print(
                f"{plant['name']}: healthy (water: {plant['water_level']}, "
                f"sun: {plant['sunlight_hours']})"
                )


# TESTS
print("=== Garden Management System ===")

plant_manager = GardenManager()
try:
    plant_manager.add_plant("rose", 3, 6)
    plant_manager.add_plant("tomato", 1, 10)
    plant_manager.add_plant("lettuce", 3, 13)
    plant_manager.add_plant("", 0, 0)
except GardenError as e:
    print("Caugh an error:", e)

print("\nWatering plants...")
try:
    plant_manager.water_plant()
except WaterError as e:
    print("Caugh WaterError:", e)


print("\nChecking plant health")
try:
    plant_manager.check_plant_health()
except PlantError as error:
    print("Caught a PlantError:", error)
finally:
    print("System recovered and continuing...")
