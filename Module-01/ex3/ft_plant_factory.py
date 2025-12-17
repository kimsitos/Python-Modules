#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


plants = [
    Plant("Rose", 47, 4),
    Plant("Sunflower", 3, 79),
    Plant("Cactus", 15, 40),
    Plant("daisy", 5, 27),
    Plant("mint", 8, 7),
    Plant("orchid", 30, 15),
]

number_plants = 0
for plant in plants:
    print("Created:", end=' ')
    plant.get_info()
    number_plants += 1

print("\nPlants created:", number_plants)
