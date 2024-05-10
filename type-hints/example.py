# pylint: disable=C0114
from typing import Union


def add_numbers(*args: Union[int, float]) -> Union[int, float]:
    """Add any number of entered numbers.

    Args:
        args (Union[int, float]): Numbers to be added.

    Returns:
        Union[int, float]: Sum of the numbers.

    Raises:
        TypeError: If any element in args is not int or float.
    """
    # Check if all arguments are either int or float
    if not all(isinstance(num, (int, float)) for num in args):
        raise TypeError("All arguments must be integers or floats")

    # Calculate the sum of numbers
    result = sum(args)
    return result
