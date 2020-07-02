# Given a string. Character “h” is included as minimal two times.
# Delete from given string first and last h - characters and all characters between them.


def delete_fragment(string):
    first_index = 0
    last_index = 0

    index = 0
    while index < len(string):
        if string[index] == 'h':
            first_index = index
            break
        index += 1

    index = len(string) - 1
    while index >= 0:
        if string[index] == 'h':
            last_index = index
            break
        index -= 1

    return f'{string[:first_index]}{string[last_index + 1:]}'

print(delete_fragment('hqwertyuhasdfghzxcvbnhmh'))
