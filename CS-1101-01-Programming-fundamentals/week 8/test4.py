# Write a new file with three entries of my kids
# Containing their name as key, year of birth and sex
with open('myKids.txt', 'w') as fout:
    fout.write('Ammad: 2012, male\n'
            'Sohaib: 2015, male\n'
            'Osaid: 2018, male\n')

with open('myKids.txt', 'a+') as fout:
    fout.write(
        'Ibrahim: 2022, male\n'
        'Ahmed: 1988, male\n'
        'Amina: 1987, female\n'
    )

