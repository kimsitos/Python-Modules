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


rose = Plant("Rose", 47, 4)
sunflower = Plant("Sunflower", 3, 79)
cactus = Plant("Cactus", 15, 40)

plants = [rose, sunflower, cactus]

initial_heigh = []
print("=== Day 1 ===")
for plant in plants:
    plant.get_info()
    initial_heigh.append(plant.height)

days = 1
while days < 7:
    for plant in plants:
        plant.age()
        plant.grow()
    days += 1

print("=== Day 7 ===")
i = 0
for plant in plants:
    plant.get_info()
    print(f"Growth this week: +{plant.height - initial_heigh[i]}")
    i += 1
