# The function append_e takes an argument and appends string "e" to it.
# The parameter "a" in append_e(a) contains reference to object "list".
def append_e(a):
    a.append("e")

list = ["a", "b", "c", "d"]
# Calling the function with object list as argument.
append_e(list)
# Printing the result. The result is ['a', 'b', 'c', 'd', 'e']
# Variable list is updated now. "e" is appended.
print(list)