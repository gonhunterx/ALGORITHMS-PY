import itertools

# Define a function to calculate the sum of two numbers
def add_numbers(a, b):
    return a + b

# Create a list of tuples containing pairs of numbers
numbers = [(1, 2), (3, 4), (5, 6)]

# Use starmap() to apply the add_numbers function to each pair of numbers
result = set(itertools.starmap(add_numbers, numbers))

# Print the result
print(result)
