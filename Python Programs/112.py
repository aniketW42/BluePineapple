# Write a python function to find the perimeter of a cylinder.

def perimeter_of_cylinder(radius: float, height: float) -> float:
    perimeter = 2 * (2 * radius + height)
    return perimeter


if __name__ == "__main__":
    print(perimeter_of_cylinder(3, 5))
