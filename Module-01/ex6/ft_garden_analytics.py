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
        print(f"- {self.name}: {self.height}cm, {self.days} days old")


class FloweringPlant(Plant):
    def __init__(self, name, height, days, colour):
        super().__init__(name, height, days)
        self.colour = colour

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.days} days old,", end='')
        print(f" {self.colour} flowers")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, days, colour, prize_points):
        super().__init__(name, height, days, colour)
        self.prize_points = prize_points

    def get_info(self):
        print(f"- {self.name}: {self.height}cm, {self.days} days old,", end='')
        print(f" {self.colour} flowers, Prize points: {self.prize_points}")


class GardenManager:
    gardens = {}
    __total_gardens = 0

    class GardenStats:
        __total_gardens = 0
        __regular_plants = 0
        __flowering_plants = 0
    
    
    def __init__(self, garden_name):
        self.garden_name = garden_name.capitalize()
        self.plants = []
        GardenManager.__total_gardens += 1
        GardenManager.gardens[self.garden_name] = self.plants

    def add_plant(self, name, height, days, colour):
        plant = Plant(name, height, days)
        self.plants.append(plant)
        GardenManager.gardens[self.garden_name].append(plant)
        self.GardenStats.__regular_plants += 1
        print(f"Added {name.capitalize()} to {self.garden_name}'s garden")

    def add_flowering_plant(self, name, height, days, colour):
        flower = FloweringPlant(name, height, days, colour)
        self.plants.append(flower)
        GardenManager.gardens[self.garden_name].append(flower)
        self.GardenStats.__flowering_plants += 1
        print(f"Added {name.capitalize()} to {self.garden_name}'s garden")

    def grow_all(self):
        print(f"\n{self.garden_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow
            print(plant.name, "grew 1cm")

    def report(self):
        print(f"\n=== {self.garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()



print("=== Garden Management System Demo ===\n")
Amaia = GardenManager("Amaia")
El_Bosco = GardenManager("El_Bosco")
Amaia.add_flowering_plant("rose", 30, 4, "rose")
El_Bosco.add_flowering_plant("violet", 30, 4, "violet")
Amaia.report()
Amaia.grow_all()
