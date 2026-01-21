#!/usr/bin/env python3

def garden_operations():
    """
    Trigger common Python exceptions intentionally.

    This function demonstrates different types of runtime errors by:
    - Attempting to convert an invalid string to an integer.
    - Dividing a number by zero.
    - Opening a file that does not exist.
    - Accessing a missing key in a dictionary.

    The function is meant for demonstration purposes only and does not
    handle the exceptions internally.
    """
    int("abc")
    1 / 0
    open("NotAFile.txt")
    {"value_01": "hola"}["jardincito"]


def test_error_types():
    """
    Demonstrate how to capture and handle different exception types.

    This function:
    - Shows how each specific error type can be caught using try/except.
    - Prints a clear message explaining what went wrong for each error.
    - Demonstrates that the program continues executing after handling errors.
    - Shows how multiple exception types can be captured using a single
      except block.
    """
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError", e)

    print("\nTesting ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError", e)

    print("\nTesting FileNotFoundError...")
    try:
        open("NotAFile.txt")
    except FileNotFoundError as e:
        print("Caught FileNotFound:", e)

    print("\nTesting KeyError...")
    try:
        {"value_01": "hello"}["Error_Key"]
    except KeyError as e:
        print("Caught KeyError:", e)

    print("\nTesting Multiple errors together...")
    try:
        1 / 0
        int("hello")
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!")


test_error_types()
