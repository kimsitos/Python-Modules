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

    def __init__(self, plant_name, water_level, sunlight_hours):
        """Initialize a plant and validate its parameters."""
        self.plant_name = 0
        if not plant_name.strip():
            raise GardenError("Plant name empty")
        self.plant_name = plant_name

        self.water_level = 0
        if water_level < 1 or water_level > 10:
            raise GardenError("Not reasonable water level")
        self.water_level = water_level

        self.sunlight_hours = 0
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise GardenError("The sunlight hours is not reasonable")
        self.sunlight_hours = sunlight_hours
        print(f"Added {plant_name} succesfully")

    def water_plant(self):
        """Water the plant, decrease water level, raise error if not enought"""
        if not self.water_level >= 1:
            raise WaterError(f"Not enough water for {self.plant_name}")
        print(f"Watering {self.plant_name} succesfully")
        self.water_level -= 1

    def check_plant_health(self):
        """Check plant's health and raise error if conditions are invalid."""
        if not self.plant_name.strip():
            raise PlantError("Not a good name for the plant")
        if self.water_level < 1 or self.water_level > 10:
            raise PlantError(f"{self.water_level} is not a good water level")
        if self.sunlight_hours < 2 or self.sunlight_hours > 12:
            raise PlantError(f"{self.sunlight_hours}h of sunlight is not good")
        print(
            f"{self.plant_name}: healthy (water: {self.water_level}, sun: "
            f"{self.sunlight_hours})"
            )


# TESTS
print("=== Garden Management System ===")

plants = []
print("\nAdding plants to garden...")
try:
    plants.append(GardenManager("rose", 5, 12))
except GardenError as error:
    print("Caught GardenError:", error)

try:
    plants.append(GardenManager("tomato", 2, 5))
except GardenError as error:
    print("Caught GardenError:", error)

try:
    plants.append(GardenManager("  ", 5, 12))
except GardenError as error:
    print("Caught GardenError:", error)


print("\nWatering plants...")
try:
    for plant in plants:
        plant.water_plant()
except WaterError as error:
    print("Caught WaterError:", error)
finally:
    print("closing watering system (cleanup)")


print("\nChecking plant health")
try:
    for plant in plants:
        plant.check_plant_health()
except PlantError as error:
    print("Caught a PlantError:", error)
