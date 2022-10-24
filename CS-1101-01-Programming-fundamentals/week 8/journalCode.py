# My string with 3 entries
my_family = {'Ahmed': ['Father'],
 'Amina': ['Mother'],
 'Ammad': ['FirstSon']
 }

# Writing "The input file for your original dictionary (with at least six items)."
with open('file1.txt', 'w') as fout1: 
    fout1.write("{\n")
    for k in sorted(my_family.keys()):
        fout1.write("'%s': %s, \n" %(k, my_family[k]))
# Not mandatory to close the file when writing using "with" but doing it as a good practice.
    fout1.close()

# Append 3 more entries, making it a dict containing 6 entries.
with open('file1.txt', 'a+') as fout2:
    fout2.write("'Sohaib': ['SecondSon'], \n"        
    "'Osaid': ['ThirdSon'], \n"       
    "'Ibrahim': ['FourthSon'] \n")
    fout2.write('}')
    fout2.close()


# Read the file, and print the file
# Doing this before inverting.
dict_from_file = []  
with open('file1.txt', 'r') as inf:
    dict_from_file = eval(inf.read())
    print('List before inverting:')
    print(dict_from_file)
print()

# Function to invert the dict
# Dictionary as argument.
def invert_dict(d):
    # Intializing variable inverse as type dict
    inverse = dict()
    # Looping over the dictionary
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:                
                inverse[item] = [key]            
            else:                
                inverse[item].append(key)
    # Printing the inverted dict as a string
    print('List after inverting:')
    print(str(inverse))
    # Appending the inverted dictionary to inverted.txt
    with open('inverted.txt','w') as finverted:
        finverted.write(str(inverse))

invert_dict(dict_from_file)