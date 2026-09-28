# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print("List:", squares)

# Dictionary comprehension
square_dict = {x: x * x for x in numbers}
print("Dictionary:", square_dict)

# Set comprehension
even_set = {x for x in numbers if x % 2 == 0}
print("Set:", even_set)
