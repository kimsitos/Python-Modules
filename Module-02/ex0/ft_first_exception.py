#!/usr/bin/env python3
def check_temperature(temp_str):
    """
    Check if a given temperature value is suitable for plants.

    The function receives a string representing a temperature, attempts to
    convert it to an integer, and validates whether it falls within the
    acceptable range for plants (0°C to 40°C inclusive).

    If the value is invalid or out of range, an error message is printed.
    If the temperature is valid, a confirmation message is printed and the
    temperature is returned as an integer.

    Args:
        temp_str (str): Temperature value provided as a string.

    Returns:
        int | None: The temperature as an integer if valid, otherwise None.
    """
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if temp_int < 0:
        print(f"Error, {temp_int}ºC is too cold for plants (min 0ºC)")
        return
    elif temp_int > 40:
        print(f"Error, {temp_int}ºC is too hot for plants (max 40ºC)")
        return
    else:
        print(f"Temperature {temp_int}ºC is perfect for plants!")
        return temp_int


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    print("\nTesting temperature: 25")
    check_temperature("25")

    print("\nTesting temperature: abc")
    check_temperature("abc")

    print("\nTesting temperature: 100")
    check_temperature("100")

    print("\nTesting temperature: -50")
    check_temperature("-50")

    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
