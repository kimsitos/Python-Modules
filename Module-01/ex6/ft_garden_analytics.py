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
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.total_growth = 0
            self.regular = 0
            self.flowering_plants = 0
            self.prize_flowers = 0
            self.points = 0

        def type_plants(self):
            print("\nPlants added:", self.flowering_plants + self.prize_flowers + self.regular)
            print(f"Plant types: {self.regular} regular, ", end='')
            print(f"{self.flowering_plants} flowering, ", end='')
            print(f"{self.prize_flowers} prize flowers")
        
        def grow_stats(self):
            print(f"\nPlants grew a total of {self.total_growth}cm")
    
    
    def __init__(self, garden_name):
        self.garden_name = garden_name.capitalize()
        self.stats = GardenManager.GardenStats()
        self.plants = []
        GardenManager.total_gardens += 1
        GardenManager.gardens[self.garden_name] = self

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.regular += 1
        print(f"Added {plant.name} to {self.garden_name}'s garden")

    def add_flowering_plant(self, flower):
        self.plants.append(flower)
        self.stats.flowering_plants += 1
        print(f"Added {flower.name} to {self.garden_name}'s garden")

    def add_prize_flower(self, prize_flower):
        self.plants.append(prize_flower)
        self.stats.prize_flowers += 1
        self.stats.points += prize_flower.prize_points
        print(f"Added {prize_flower.name} to {self.garden_name}'s garden")

    def grow_all(self):
        print(f"\n{self.garden_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1
            print(plant.name, "grew 1cm")
        print("")

    def report(self):
        print("")
        print(f"=== {self.garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()

    @classmethod
    def resume_scores(cls):
        print(f"\nTotal gardens managed: {cls.total_gardens}")
        print(f"Garden scores - ", end='')
        for garden in cls.gardens.values():
            print(f"{garden.garden_name}: {garden.stats.points}", end=' ')
        print("")
    
    @classmethod
    def resume_gardens(cls):
        for garden in cls.gardens.values():
            garden.report()
            garden.stats.grow_stats()
            garden.stats.type_plants()

    @classmethod
    def create_garden_network(cls):
        network = []
        for garden in cls.gardens.values():
            network.append(garden.garden_name)
        return network


## TESTER 
print("=== Garden Management System Demo ===")

# Create Garden
Amaia = GardenManager("Amaia")
El_Bosco = GardenManager("El_Bosco")
print("Garden network:", GardenManager.create_garden_network(), "\n")


# Add plants
Amaia.add_flowering_plant(FloweringPlant("rose", 30, 4, "rose"))
Amaia.add_prize_flower(PrizeFlower("violet", 5, 2, "green", 50))
Amaia.add_prize_flower(PrizeFlower("sunflower", 30, 63, "yellow", 50))

El_Bosco.add_flowering_plant(FloweringPlant("violet", 30, 4, "violet"))
El_Bosco.add_plant(Plant("mint", 3, 50))

# Amaia stats
Amaia.report()
Amaia.grow_all()
Amaia.stats.type_plants()

# Garden stats
GardenManager.resume_gardens()
GardenManager.resume_scores()
