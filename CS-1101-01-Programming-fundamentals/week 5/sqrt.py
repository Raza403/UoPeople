# Defining the function
def my_sqrt(a):
    # Choosing the value for x
    x = 3
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y

# Returning the value
    return y

# Calling the function, and saving the return value in variable result.
result = my_sqrt(6)
# Printing the result
print(result)