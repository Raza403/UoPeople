# This function will divide when provided by a dividend and a divisor
def divide(dividend, divisor):
    # Division is taking place here
    divided = dividend/divisor
    # Value along with a string statement is being returned here.
    # Note: ERROR HERE
    # In Python, string, and Int cannot be concatenated. This is perfectly fine in JavaScript but not in the Python.
    ans = "The answer of " + dividend + " divided by divisor " + divisor + " is " + divided
    return(ans)
    # In python, the correct statement is below. We have to convert int to string usign str()
    # Below we have a right statement.
    # ans = "The answer of " + str(dividend + " divided by divisor " + str(divisor) + " is " + str(divided)
    # return(ans)

# Calling the function with arguments.
answer = divide(6,2)
# Printing the value of the returned value, ie. answer.
print(answer)
