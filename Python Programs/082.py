#Write a function to find the volume of a sphere.
import math
def volumeOfsphere(r):

    volume = 4/3*math.pi*math.pow(r, 3)

    return volume

print(volumeOfsphere(5))