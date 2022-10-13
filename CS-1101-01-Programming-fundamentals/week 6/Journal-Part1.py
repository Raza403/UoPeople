# A string containing my kids names with spaces between them.
myKids = "Ammad Sohaib Osaid Ibrahim"
# Converting from string to list using split method.
myKidsList = myKids.split(" ") # ['Ammad', 'Sohaib', 'Osaid', 'Ibrahim']
print("Converting from string to list using split method.")
print(myKidsList)
print("-----------------") # Just a separator.

# Sorted the list using sort method.
myKidsList.sort() # ['Ammad', 'Ibrahim', 'Osaid', 'Sohaib']
print("Sorted the list using sort method.")
print(myKidsList)
print("------------------------")

# Removed last name using .pop method
myKidsList.pop() # ['Ammad', 'Ibrahim', 'Osaid']
print("Removed last name using .pop method")
print(myKidsList)
print("------------------------")
# Removed last name using remove method.
myKidsList.remove("Osaid") # ['Ammad', 'Ibrahim']
print('Removed last name using remove method.')
print(myKidsList)
print("--------------------")

# Removed item at index 1 which is second item using del
del myKidsList[1] # ['Ammad']
print("Removed item at index 1 which is second item using del")
print(myKidsList)
print("----------------------------------")

# Adding "Appended" in the list using append method.
myKidsList.append("Appended") # ['Ammad', 'Appended']
print('Adding "Appended" in the list using append method.')
print(myKidsList)
print("--------------------------------")
# Adding "AddAnother" using index of the list
myKidsList[1] = "AddAnother" # ['Ammad', 'AddAnother']
print('Adding "AddAnother" using index of the list')
print(myKidsList)
print("-----------------------------------")
# Initializing a list myName
myName = ["Ahmed"]
# Adding myName to myKidsList using addition.
myKidsList = myKidsList + myName # ['Ammad', 'AddAnother', 'Ahmed']
print("Adding using + operator")
print(myKidsList)
print("--------------------------------------")
# Adding space as delimiter
delimiter = ' '
# Joining myKidsList with delimiter, and saving the value ot myKids
myKids = delimiter.join(myKidsList) # "Ammad AddAnother Ahmed"
print("Joining myKidsList with delimiter, and saving the value ot myKids")
print(myKids)