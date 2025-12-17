#Write a python function to find the volume of a triangular prism.
import math
def volumeOfTriangularPrism(s1, s2, s3, h):
    semiperi = (s1+s2+s3)/2
    area = math.sqrt(semiperi*(semiperi-s1)*(semiperi-s2)*(semiperi-s3))
    volume = area * h
    return volume

print(volumeOfTriangularPrism(3,4,5,10))