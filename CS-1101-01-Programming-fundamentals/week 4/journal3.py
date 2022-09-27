import math
# The function accepts two arguments to calculate
# the value of a right angle triangle's hypotenuse
def hypotenuse(a,b):
    # Calculating the final result now.
    result = math.sqrt(a**2+b**2)
    # Return the result 
    return(result)

# A function call with parameters.
Length = hypotenuse(2,3)
# Print the result.
print(Length)