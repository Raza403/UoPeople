# This function calculates the perimeter of rectangle
# The formula is "2(l + b)". Where ‘l’ is Length and ‘b’ is Breadth
def perimeter(l,b):
    # Calculating result by adding Length and Breadth as an initial step
    result = 2*(l+b)
    # Return the result
    return result

# Calling the function with parameters
answer = perimeter(4,3)
print(answer)