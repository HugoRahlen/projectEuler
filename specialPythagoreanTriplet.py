# Finds the pythagorean triplet a + b + c = 1000
import math

def cycle():
    for i in range(1, 1000):
        for j in range(1, 1000):
            c = math.sqrt(i * i + j * j)
            if i + j + c == 1000:
                return i * j * c

print(cycle())
