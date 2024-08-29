"""
This module contains a simple function to add two numbers.
"""


def add(first_number, second_number):
    """
    Add two numbers and return the result.

    Args:
        first_number (int or float): The first number.
        second_number (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return first_number + second_number


PRAC = add(1, 2)
print(f"This is the sum: 1, 2, {PRAC}")
