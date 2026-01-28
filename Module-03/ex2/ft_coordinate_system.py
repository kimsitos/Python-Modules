#!/usr/bin/env python3

# -------------------
# NECESITA REVISION
# -------------------

import math


def parsing(position: tuple) -> tuple:

    temp = position[1:-1]
    coordinate = temp.split(',')

    i = 0
    for number in coordinate:
        i += 1
    if i != 3:
        print("Expected 3 numbers, recibed", i)
        return

    try:
        return tuple((
            float(coordinate[0]),
            float(coordinate[1]),
            float(coordinate[2])))
    except ValueError:
        print("Error parsing. Invalid format for int")


def distance(start: tuple, end: tuple):
    return math.sqrt(
        (end[0]-start[0])**2 +
        (end[1]-start[1])**2 +
        (end[2]-start[2])**2)


position_start = tuple((0, 123, 4))
position_end = tuple((0, 0, 0))

if position_start:
    print("Unpacking demonstration:")
    print(
        f"Player at x={position_start[0]},",
        f"y={position_start[1]},",
        f"z={position_start[2]}"
        )

    print(
        f"Final coordinates x={position_end[0]},",
        f"y={position_end[1]},",
        f"z={position_end[2]}"
    )
    print(distance(position_start, position_end))
