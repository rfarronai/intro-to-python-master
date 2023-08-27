"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""

from math import pi


def area(r):
    return pi * r ** 2


def circumference(r):
    return pi * r * 2


radius = int(input("Circle radius: "))

print(f'Area: {round(area(radius), 2)}')  # <-- Call the area function and print the result
print(f'Circumference: {round(circumference(radius), 2)}')  # <-- Call the circumference function and print
