# Write a function to find the circumference of a circle.
from math import pi

def circumference_of_circle(radius: float) -> float:

    return 2 * pi * radius

if __name__ == "__main__":
    print(circumference_of_circle(5))
    print(circumference_of_circle(5.5))