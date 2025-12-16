#!/usr/bin/env python3

class class_plant:
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
    class_plant("Rose", 47, 4),
    class_plant("Sunflower", 3, 79),
    class_plant("Cactus", 15, 40),
    class_plant("daisy", 5, 27),
    class_plant("mint", 8, 7),
    class_plant("orchid", 30, 15),
]

number_plants = 0
for plant in plants:
    print("Created:", end=' ')
    plant.get_info()
    number_plants += 1

print("\nPlants created:", number_plants)
