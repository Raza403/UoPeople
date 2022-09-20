def checkNumber(n):
    # Check if the number is negative?
    if (n < 0):
        print("The nubmer is negative")
    else:
        if(n == 0):
            print("The nubmer is 0.")
        elif(0 < n < 10):
            print("The number is a sigle digit positive integer.")
        else:
            print("The nubmer is 2 or more digits positive integer.")

num = input("Please enter a positive number\n")
# Converting input to an int.
checkNumber(int(num))