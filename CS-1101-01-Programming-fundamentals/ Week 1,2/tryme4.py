# Printing new line
from itertools import combinations


def new_line():

    print('.')

# Using new_line() function 3 times to print 3 lines.
def three_lines():

    new_line()

    new_line()

    new_line()

# Using three_lines() function 3 times to print total 9 lines.
# NOTE: three_lines() here is an example of using nested function
def nine_lines():
    three_lines() # 3 lines 
    three_lines() # 6 lines
    three_lines() # 9 lines

print("Printing nine lines.")
# Printing 9 lines by calling nine_lines() function.
nine_lines()
    
# Using a combination of nine_lines(), three_lines(),
# and new_line(), the function clear_screen() prints 25 lines.
def clear_screen():
    new_line() # 1 line
    three_lines() # 4 lines
    three_lines() # 7 lines
    nine_lines() #16 lines
    nine_lines() # 25 lines

print("Printing 25 lines.")
# Printing 25 lines
clear_screen()