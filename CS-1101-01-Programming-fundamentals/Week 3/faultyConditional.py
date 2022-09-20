def checkNumber(n):
    # Checks if number is 0
    if( n == 0):
        print("You entered a 0.")
    # in case number is greater than 0, this branch will execute because
    # the statement "n > 0" is true. Next all the branches (n > 10) or (n > 100)
    # won't execute. Even if we enter a number 999.
    if (n > 0):
        print("You entered a positive number.")
    # Even if n == 11, this code won't execute because the statement above (n > 0) 
    # will execute.
    elif (n > 10):
        print("The number is greater than 10")
    elif (n > 100):
        print("The number is greater than 100.")
    # This code will execute if user enters a negative number.
    else:
        print("You entered a negative number.")

num = input("Please enter a positive number\n")
# Converting input to an int.
checkNumber(int(num))