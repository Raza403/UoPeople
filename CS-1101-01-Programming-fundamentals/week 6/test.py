letters = ["a", "b", "c", "d"]
numbers = [1,2,3,4]
# Nested list
letters.append(numbers) # ['a', 'b', 'c', 'd', [1, 2, 3, 4]]
print("Nested list")
print(letters)
print("-----------------") # Just for separation.

# The “*” operator 
# Multiplication using * operator, the list will be repeated twice.
numbers = numbers * 2 # [1, 2, 3, 4, 1, 2, 3, 4]
print("The '*' operator")
print(numbers)
print("-----------------")

# List slices 
# Sliced the list to half
numbers = numbers[4:8]
print("List slices")
print(numbers)
print("----------------")

# The “+=” operator 
# Initializing a variable called total with initial value 0
total = 0
for number in numbers:
    total += number # 1+2+3+4 = 10

print('The “+=” operator')
print(total) # 10
print("----------------")
# A list filter 
# Initializing an empty list to store even numbers later.
evenNumbers = []
# Filter even numbers from list numbers
for number in numbers:
    if number%2==0: # Filter the number who's modulus is 0 when divided by 2. Or even numbers
        evenNumbers.append(number) # Append those numbers to the evenNumbers list.

print("A list filter")
print(evenNumbers) # [2, 4]
print("-----------------")

# A list operation that is legal but does the "wrong" thing, and not what the programmer expects 
t1 = [1,2,3,4] # Initializing a variable list with some integers.
t2 = t1.append(5) # Appending int 5 to the list and saving it to a new variable t2.
print('A list operation that is legal but does the "wrong" thing, and not what the programmer expects')
print(t1) # The output is None. Because method append doesn't return a value.

t3 = t1.pop() # I thought this will give me [1,2,3,4]
print(t3) # Instead, the output is 5, which is the poped value only.
# I learned the return of pop() is the value it poped not the remaining value.

t4 = t1.remove(4) # Expecting the same value as in pop()
print(t4) # The output is None. remove() method doesn't return a value.
