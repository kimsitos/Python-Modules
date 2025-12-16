#!/usr/bin/env python3

class class_plant:
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days


rose = class_plant("Rose", 47, 4)
sunflower = class_plant("Sunflower", 3, 79)
cactus = class_plant("Cactus", 15, 40)

plants = [rose, sunflower, cactus]

print("=== Garden Plant Registry ===")
for plant in plants:
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old")
