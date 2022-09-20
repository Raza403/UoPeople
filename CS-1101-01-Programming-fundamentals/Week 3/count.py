# Defining a function for count up.
# This function will be called when value is negative.
def countup(n):
     # Print Blastoff when n is equal to or greater than 0.
     if n >= 0:
          print('Blastoff!')
     # Else print the value of n and count up n+1.
     else:
          print(n)
          countup(n+1)

# Defining a function for countdown.
# This function will be called when value is 0 or above.
def countdown(n):
     # Print Blastoff when n is less than or equal to 0.
     if n <= 0:
          print('Blastoff!')
     # Else print value of n and count down n-1.
     else:
          print(n)
          countdown(n-1)

# Get the value from user by showing a prompt
# Converting the input to Int so that logical operators like < or > can work.
num = int(input("Please enter a number...\n"))

# Countdown when value is greater than or equal to 0.
if(num >= 0):
    countdown(num)
# Else the value is sure to be negative, countup then.
else:
    countup(num)