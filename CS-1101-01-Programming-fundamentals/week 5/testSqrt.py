import math
# Math library is imported to use built-in math.sqrt() method

# Calculating approx sqrt
def my_sqrt(a):
    # Choosing a value for x
    x = 3
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
# Returning the value of y
    return y

def test_sqrt():
    # For 1 to 25, First number (1) is included
    # the last number (25) is not included, that's why range to 26.
    for a in range(1, 26):
        # Calculate the approx value
        mysqrt = my_sqrt(a)
        # Calculate the correct value using math.sqrt() method
        correctsqrt = math.sqrt(a)
        # Print the results
        print("a =", a,
              "approx. sqrt =", mysqrt,
              "actual sqrt =", correctsqrt,
              "difference =", abs(mysqrt - correctsqrt))

# Calling the function
test_sqrt()