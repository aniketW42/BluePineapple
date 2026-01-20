# Write a function to get the angle of a complex number.

import math
def angleOfComplexNumber(complex):
    x = complex.real
    y = complex.imag

    angle = math.atan2(y, x)

    return math.degrees(angle)


if __name__ == "__main__":
    print(angleOfComplexNumber(3 + 4j))
    print(angleOfComplexNumber(-3 + 4j))
    print(angleOfComplexNumber(3 - 4j))
    print(angleOfComplexNumber(-3 - 4j))
