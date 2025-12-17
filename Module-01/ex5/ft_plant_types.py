#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days


class Flower(Plant):
    def __init__(self, name, height, days, colour):
        super().__init__(name, height, days)
        self.colour = colour

    def bloom(self):
        print(f"{self.name} is blooming beautifuly")


class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 5 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season, nutritional_value):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


print("=== Garden Plant Types ===")

flowers = [
    Flower("rose", 12, 3, "red"),
    Flower("violet", 5, 20, "violet"),
]

for flower in flowers:
    print(f"\n{flower.name} (Flower): {flower.height}cm, ", end='')
    print(f"{flower.days}, {flower.colour} colour")
    flower.bloom()

trees = [
    Tree("oak", 570, 1560, 47),
    Tree("pine", 600, 540, 36),
]

for tree in trees:
    print(f"\n{tree.name} (Tree): {tree.height}cm, {tree.days} days, ", end='')
    print(f"{tree.trunk_diameter}cm diameter")
    tree.produce_shade()

vegetables = [
    Vegetable("tomato", 50, 30, "summer", "rich in vitamin c"),
    Vegetable("potato", 5, 35, "spring", "rich in carbohydrates"),
]

for vegetable in vegetables:
    print(f"\n{vegetable.name} (Vegetable): {vegetable.height}cm, ", end='')
    print(f"{vegetable.days} days, {vegetable.harvest_season} harvest")
    print(f"{vegetable.name} is {vegetable.nutritional_value}")
