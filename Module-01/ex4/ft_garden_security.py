#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height, days):
        self.__name = name.capitalize()
        self.__height = 0
        self.__days = 0

        self.set_height(height)
        self.set_age(days)

    def grow(self):
        self.__height += 1

    def age(self):
        self.__days += 1

    def set_height(self, height):
        if height < 0:
            print(f"Invalid negative height: {height}cm")
        else:
            self.__height = height
            print(f"height updated: {self.__height}")

    def set_age(self, days):
        if days < 0:
            print(f"Invalid negative age: {days} days")
        else:
            self.__days = days
            print(f"Age updated: {self.__days}")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__days

    def get_info(self):
        print(f"{self.__name}: {self.__height}cm, {self.__days} days old")


rose = SecurePlant("rose", -5, 6)
mint = SecurePlant("mint", 2, 0)
print("=== Before ===")
mint.get_info()
rose.get_info()

print("=== After ===")
mint.set_height(-70)
rose.set_age(3)
mint.get_info()
rose.get_info()
