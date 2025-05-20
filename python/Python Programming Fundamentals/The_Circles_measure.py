# Write a Python function using a precise descriptive name like calculate_diameter_circle while also incorporating snake case.

# The function should take one argument: radius (with a float type hint).
    
def calculate_diameter_circle(radius: float) -> float:
    """Calculates the mean of a list of numbers."""
    if radius<0:
        print ("-1")
        return -1
    elif radius == 0:
        print("0.0")
        return 0.0
    print(radius * 2)
    return radius * 2
# It should calculate the diameter of a circle (diameter = radius * 2) and return it. As there is no requirement for the radius to be a whole number, you should assume a return of float. 

# Include a clear and informative docstring explaining the function's purpose, arguments, and return value, also using type hints.

# Handle potential errors: You have been given the instructions that if the user sends in a negative radius, the function should return -1 to indicate an error.
calculate_diameter_circle(7)
calculate_diameter_circle(2.5)
calculate_diameter_circle(0)
calculate_diameter_circle(-3)
calculate_diameter_circle(1000000)