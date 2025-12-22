#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Something went wrong in the garden"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Something went wrong with the plants"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Something went wrong with the Water"):
        super().__init__(message)


def valid_height(height):
    if height < 0:
        raise PlantError("The heigh is not valid, please insert valid height")


def valid_water(water):
    if water < 2:
        raise WaterError("Not enought water in the tank")


def valid_garden(heigh, water):
    try:
        valid_height(heigh)
    except GardenError as error:
        print(f"Caught a Garden Error: {error}")
    try:
        valid_water(water)
    except GardenError as error:
        print(f"Caught a Garden Error: {error}")


valid_garden(-2, 1)
