#!/usr/bin/env python3

import math


def parsing(position: str) -> tuple:
    coordinates = tuple()
    try:
        for num in position.split(','):
            coordinates = coordinates + (int(num),)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        return

    i = 0
    for number in coordinates:
        i += 1
    if i != 3:
        print("Expected 3 numbers, recibed", i)
        return
    return coordinates


def distance(start: tuple, end: tuple):
    return math.sqrt(
        (end[0]-start[0])**2 +
        (end[1]-start[1])**2 +
        (end[2]-start[2])**2)


print("=== Game Coordinate System ===\n")

position_start = tuple((10, 20, 5))
position_end = tuple((0, 0, 0))
print("Position created:", position_start)
print(f"Distance between{position_end} and {position_start}:",
      distance(position_start, position_end))

print("\nParsing coordinaates: \"3,4,0\"")
position_start = parsing("3,4,0")
print("Parsed position:", position_start)
print(f"Distance between{position_end} and {position_start}:",
      distance(position_start, position_end))

print("\nParsing invalid coordinates: \"abc,def,ghi\"")
parsing("abc,def,ghi")
print("\nUnpacking demonstration:")
(x, y, z) = position_start
print(f"Player at x={x},",
      f"y={y},",
      f"z={z}")
