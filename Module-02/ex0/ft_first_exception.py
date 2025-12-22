#!/usr/bin/env python3
def check_temperature(temp_str):
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
