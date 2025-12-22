#!/usr/bin/env python3
from ft_first_exception import check_temperature

print("=== Garden Temperature checker===\n")
test_values = ["25", "abc", "100", "-50"]

for test in test_values:
    print("Testing temperature:", test)
    check_temperature(test)
    print()

print("All test completed - program didn't crash!")