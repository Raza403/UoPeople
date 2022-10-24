# Dict having my kids name and keys
# Their usernames, year of birth and sex as value.
myKids = {
    'ahmed': ['raza1988', 1988, 'Male'],
    'amina': ['amn1987', 1987, 'Female'],
    'Ammad': ['Amd2012', 2012, 'Male'],
    'Sohaib': ['Shb2015', 2015, 'Male'],
    'Osaid': ['Osd2018', 2018, 'Male'],
    'Ibrahim': ['Ibrm2022', 2022, 'Male'],
     }

with open('myKids_dict', 'a+') as fout:
    # Looping over all the items of myKids dict
    for key, value in myKids.items():
        # Writing file
        fout.write(f'{key}:{value}\n')
        # Printing file
        print(f'{key}:{value}\n')