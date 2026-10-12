#Import entire module
import math
print("Square root:", math.sqrt(25))

#Import specific function
from math import factorial
print("Factorial:", factorial(5))

#Import module with an alias
import random as r
print("Random number:", r.randint(1, 10))

#Import multiple functions
from math import pow, ceil
print("Power:", pow(2, 3))
print("Ceiling:", ceil(4.3))
