# The function below will calculate area of a circle
# When "r" or radius is given as an argument while calling the function.
def print_area (r):
    # Importing Math library for using built in Pi.
    import math
    # Calculating area of the circle, formula is πr2
    circleArea = math.pi * r**2
    # Print volume
    print("Input radius is " + str(r))
    print("Area of the circle for the radius " + str(r) + " is " + str(circleArea))
    # Printing a divider between each function calls
    print("---------------------------------------------------------")

# Calling print_volume() function 3 times with different value.
print_area(3)
print_area(6)
print_area(9)
