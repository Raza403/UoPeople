# Open the dict file as fout
with open('myKids_dict') as fout:
    # Initialize variable data as a dict type.
    data = dict()
    # Iterate over all the lines of file.
    for i in fout.readlines():
        # Check if it is not a new line.
        if i != '\n':
            # Split over ":"
            item = i.split(':')
            data[item[0]] = item[1].strip()
    
    # Print the data
    print(data)