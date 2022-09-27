# This function will divide when provided by a dividend and a divisor
def divide(dividend, divisor):
    # Division is taking place here
    divided = dividend/divisor
    # Value along with a string statement is being returned here.
    return("The answer of " + str(dividend) + " divided by divisor " + str(divisor) + " is " + str(divided) )

# Calling the function with arguments.
# Note: The divisor in this example is ZERO, which creates an error
# Precondition is violated here, as the problem is not with the function,
# Problem is with one of the arguments.
answer = divide(6,0)
# Printing the value of the returned value, ie. answer.
print(answer)
