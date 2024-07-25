"""
Challenge007: Write a Friday 13th detector.
Create a function in Python that accepts two parameters.
They’ll both be numbers. The first will be the month as a number,
and the second will be the four-digit year.
The function should parse the parameters and return
True if the month contains a Friday the 13th and False if it doesn’t.
"""
from datetime import date


def isFriday13(month, year):
    """
    Friday 13th detector
    """
    # weekday() return Monday is 0 and Sunday is 6
    return date(year, month, 13).weekday() == 4


if __name__ == "__main__":
    print(isFriday13(10, 2023))
    print(isFriday13(9, 2024))
    print(isFriday13(12, 2024))
