#!/usr/bin/env python3

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


def valid_height(height):
    """Checks if there is enough water."""
    if height < 0:
        raise PlantError("The heigh is not valid, please insert valid height")


def valid_water(water):
    """Checks if there is enough water."""
    if water < 2:
        raise WaterError("Not enought water in the tank")


def valid_garden(heigh, water):
    """Validates garden conditions and handles errors."""
    try:
        valid_height(heigh)
    except GardenError as error:
        print(f"Caught a Garden Error: {error}")
    try:
        valid_water(water)
    except GardenError as error:
        print(f"Caught a Garden Error: {error}")


valid_garden(-2, 1)
