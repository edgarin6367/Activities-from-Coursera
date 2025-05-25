# Write the Python code required to take a list of numbers as input and return a new list containing only the unique numbers from the original list, maintaining their original order, and then print the result.
array = [1,2,2,3,1,4,5,3]

unique_set = set(array)
unique_array = list(unique_set)
print(unique_array)
