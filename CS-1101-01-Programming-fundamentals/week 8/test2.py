# Defining the function
def str_to_dict():
    # Get the key value pair from user splited by ","
    val = input('Enter the key value pair splited by ","').split(',')
    # Sanity check for wrong inputs.
    if len(val) != 2 or not val[0] or not val[1]:
        # Show error message.
        print('Enter correct data')
        # Rerun the function to get correct data.
        return str_to_dict()
    # Add the values to dict as key value pairs
    dict_from_string = {val[0]: val[1]}
    # Print the dict
    print('dict:',dict_from_string)

str_to_dict()