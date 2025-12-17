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
    class GardenStats:
        @classmethod
        def report(cls):
            for name in cls.gardens:
                print(f"\n=== {name}'s Garden Report ===")
                print("Plants in garden:")
                for plant in cls.gardens[name]:
                    plant.get_info()
            print("\nTotal gardens managed:", cls.__total_gardens)

    def __init__(self, garden_name):
        self.garden_name = garden_name.capitalize()
        self.plants = []
        GardenManager.__total_gardens += 1
        GardenManager.gardens[garden_name.capitalize()] = []

    def add_plant(self, name, height, days, colour):
        plant = Plant(name, height, days)
        self.plants.append(plant)
        GardenManager.gardens[self.garden_name].append(flower)
        print(f"Added {name.capitalize()} to {self.garden_name}'s garden")
        GardenManager.__regular_plants += 1

    def add_flowering_plant(self, name, height, days, colour):
        flower = FloweringPlant(name, height, days, colour)
        self.plants.append(flower)
        GardenManager.gardens[self.garden_name].append(flower)
        print(f"Added {name.capitalize()} to {self.garden_name}'s garden")
        GardenManager.__flowering_plants += 1

    def grow(self):
        print(name, "is helping all plants grow...")
        for plant in self.plants:
            plant.grow
            print(plant.name, "grew 1cm")

    @classmethod
    # def create_garden_netwok():
    #     garde
    



print("=== Garden Management System Demo ===")
Amaia = GardenManager("Amaia")
El_Bosco = GardenManager("El_Bosco")
# Dennis = GardenManager.create_garden_netwok()
Amaia.add_flowering_plant("rose", 30, 4, "rose")
El_Bosco.add_flowering_plant("violet", 30, 4, "violet")
GardenManager.GardenStats()
