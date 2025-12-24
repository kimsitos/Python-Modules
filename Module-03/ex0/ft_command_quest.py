#!/usr/bin/env python3

import sys

print("=== Command Quest ===")

arguments = sys.argv
num_arg = len(arguments)

if num_arg == 1:
    print("No arguments provided")

print(f"Program name: {arguments[0]}")
print(f"Arguments recived: {num_arg - 1}")
i = 1
for arg in arguments[1:]:
    print(f"Argument {i}: {arg}")
    i += 1

print(f"Total arguments: {num_arg}")