#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plant1 = Plant("Rose", 47, 4)
plant2 = Plant("Sunflower", 3, 79)
plant3 = Plant("Cactus", 15, 40)
print("=== Garden Plant Registry ===")
print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
