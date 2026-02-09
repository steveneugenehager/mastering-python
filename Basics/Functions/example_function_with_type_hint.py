# example_function_with_type_hint.py
"""Simplest illustration of defining a function with type hints and a function docstring."""
import math

def main() -> None:
    """Entry point for the script logic."""

    print( calculate_square_root(6.25) )

def calculate_square_root(number: float) -> float:
    """
    Computes the square root of a non-negative number.

    Args:
        number: The numeric value (int or float) to calculate the square root of.

    Returns:
        The square root of the input as a float.

    Raises:
        ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    
    return math.sqrt(number)


if __name__ == "__main__":
    main()