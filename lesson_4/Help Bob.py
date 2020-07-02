# He needs you to create a method that can determine how many letters and digits are in a given string.


def help_bob(string):
    counter = 0
    for character in string:
        if character.isalnum():
            counter += 1
    return counter

print(help_bob('hel2!lo'))
print(help_bob('wicked .. !'))
print(help_bob('!?..A'))
print(help_bob('asd1?>DSA'))
