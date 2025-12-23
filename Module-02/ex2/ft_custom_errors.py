#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base exception class for garden-related errors.

    This exception represents general problems that may occur
    in the garden and serves as a parent class for more specific
    garden exceptions.
    """
    def __init__(self, message="Something went wrong in the garden"):
        super().__init__(message)


class PlantError(GardenError):
    """
    Exception raised for plant-related problems.

    This error is used when an issue occurs related to plant
    conditions, such as invalid plant height.
    """
    def __init__(self, message="Something went wrong with the plants"):
        super().__init__(message)


class WaterError(GardenError):
    """
    Exception raised for watering-related problems.

    This error is used when an issue occurs related to watering,
    such as insufficient water levels.
    """
    def __init__(self, message="Something went wrong with the Water"):
        super().__init__(message)


def valid_height(height):
    """
    Validate the height of a plant.

    Raises a PlantError if the provided height value
    is not valid.
    """
    if height < 0:
        raise PlantError("The heigh is not valid, please insert valid height")


def valid_water(water):
    """
    Validate the amount of water available.

    Raises a WaterError if the water amount is insufficient.
    """
    if water < 2:
        raise WaterError("Not enought water in the tank")


def valid_garden(heigh, water):
    """
    Validate overall garden conditions.

    This function checks both plant height and water level.
    It demonstrates how GardenError can be used to catch
    all garden-related exceptions, including PlantError
    and WaterError, allowing the program to continue
    execution after handling errors.
    """
    try:
        valid_height(heigh)
    except GardenError as error:
        print(f"Caught a Garden Error: {error}")
    try:
        valid_water(water)
    except GardenError as error:
        print(f"Caught a Garden Error: {error}")


valid_garden(-2, 1)
