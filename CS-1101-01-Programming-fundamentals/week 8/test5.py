# Function defined to read the dict and return a dictionary.

def read_dict(fileName):
    # Initialize a dict
    dictionary={}
    # Open file as read only.
    with open(fileName,'r') as fin:
        # for loop to read all the lines of the file.
        for line in fin.readlines():
            # Strip the line and split using ':'
            items = line.split()
            print(items)
            line = line.strip().split(':')
            # print(line)
            # Assign key
            key = line[0].strip('\'')
            # print(key)
            # Assign values
            values = [item.strip('\'') for item in line[1].strip('[]').split(',')]
            # Add values to key.
            dictionary[key]=values
            # print(dictionary)
            return dictionary

# Function definition for inverted dictionary.
def invert_dict(d):
    inverted={} 
    for key, items in d.items(): 
        for item in items: 
            inverted[item]=key 
            return inverted

# Takes inverted dictionary and saves it to filename provided as argument.
def write_to_file(inverted_dictionary,filename):
    # Open the file with write permission as fout
    with open(filename,'w') as fout:
        # Loop over inverted dictionary for key and value.
        for key,value in inverted_dictionary.items():
            # Write the key, value pairs
            fout.write('\'{0}\':[\'{1}\']\n'.format(key,value))
            # Print the success message.
            print('{} updated successfully.'.format(filename))

def main():
    infile_name = 'dictionary.txt' # file that needs to be read from 
    d = read_dict(infile_name) # reads the file which returns a dictionary
    reversed_d = invert_dict(d) # reverses the dictionary and return the reversed dictionary
    print(reversed_d) # you can comment this line
    outfile_name='inverted_dict.txt' # file that needs to be updated with the reversed dictionary
    write_to_file(reversed_d,outfile_name) # writes dictionary to the file

main()