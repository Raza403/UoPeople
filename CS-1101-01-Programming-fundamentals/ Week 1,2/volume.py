def print_volume (r):
    # Importing Math library for using built in Pi.
    import math
    # Calculating volume of the sphere
    volume = 4/3 * math.pi * r**3
    # Print volume
    print (volume)
    # A divider to seperate 3 function calls.
    print("------------------")

# Calling print_volume() function 3 times with different value.
print_volume(3)
print_volume(6)
print_volume(9)
