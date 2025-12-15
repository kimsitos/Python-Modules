#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plant1 = Plant("Rose", "36cm", "4 days")
print("=== Garden Plant Registry ===")
print(plant1.name, plant1.height, plant1.age)
