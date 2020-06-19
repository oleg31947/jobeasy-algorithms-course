# User enter a string from a keyboard. Result for return - inverted string

# string1 = input(f"Enter a string: ")


def reversed_string(string):
    # option 1
    # return string[::-1]
    # option 2
    # return ''.join(reversed(string))
    # option 3
    result = ''
    index = len(string)
    while index > 0:
        result += string[index - 1]
        index -= 1
    return result


# print(reversed_string(string1))
