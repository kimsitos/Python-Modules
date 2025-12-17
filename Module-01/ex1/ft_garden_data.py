#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days


rose = Plant("Rose", 47, 4)
sunflower = Plant("Sunflower", 3, 79)
cactus = Plant("Cactus", 15, 40)

plants = [rose, sunflower, cactus]

print("=== Garden Plant Registry ===")
for plant in plants:
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old")
