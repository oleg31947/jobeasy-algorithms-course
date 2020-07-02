# Isogram is a word with no repeating letters, in a row or not. Create a Python function to check is word isogram.
# Empty string - isogram. Case doesn’t matter.


def is_isogram(string):
    if len(string) == 0:
        return True
    string = string.upper()
    unic = ''
    for character in string:
        if character in unic:
            return False
        unic += character
    return True


print(is_isogram('world'))
