def repeatName(first, last): # function with 2 parameters.
    fullName = first + " " + last # A local variable, available inside the function only.
    print(fullName)

# Trying to print the variable fullName outside the function
try: # print fullName variable.
    print(fullName)
except: # If there is any error show this error message.
    print("Variabel fullName is available inside the function repeatName() only")
