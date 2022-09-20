def checkNumber(n):
    # Checks if number is 0
    if( n == 0):
        print("You entered a 0.")
    # Check if number is greater than 100?
    elif (n > 100):
        print("The number is greater than 100.")
    # Or the number is greater than 10?
    elif (n > 10 ):
        print("The number is greater than 10")
    # Or it is at least a positive number, greater than 0
    elif (n > 0):
        print("You entered a positive number.")
    # Else this must be a negative number
    else:
        print("You entered a negative number.")

num = input("Please enter a positive number\n")
# Converting input to an int.
checkNumber(int(num))