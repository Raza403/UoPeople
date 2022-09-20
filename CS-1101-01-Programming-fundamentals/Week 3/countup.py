# Defining a countup function.
def countUp(n):
     # Print Blastoff when n is equal to or greater than 0.
     if n >= 0:
          print('Blastoff!')
     # Else print the value of n, and count up n+1.
     else:
          print(n)
          countUp(n+1)

# Call the function with an argument -3
countUp(-3)