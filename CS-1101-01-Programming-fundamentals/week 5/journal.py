prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    # If the letter is "O" or "Q" add a u between the letter and suffix
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    # Else print letter and suffix
    else:
        print(letter + suffix)
