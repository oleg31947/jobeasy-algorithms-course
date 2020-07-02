# TODO: Write a function for decompressing string “a4b3c2d”


# def decompress(string):
#     result = ''
#     number = ''
#     counting = False
#
#     index = len(string) - 1
#
#     while index >= 0:
#         if string[index].isdigit():
#             if string[index - 1].isdigit():
#                 number += string[index]
#                 counting = True
#             else:
#                 if not counting:
#                     result += string[index - 1] * int(string[index])
#                     index -= 1
#                     number = ''
#                 else:
#                     number += string[index]
#         else:
#             if counting:
#                 result += string[index] * int(''.join(reversed(number)))
#                 counting = False
#                 number = ''
#             else:
#                 result += string[index]
#         index -= 1
#     return ''.join(reversed(result))
#
#
# print(decompress('a100b222c'))


def decompress_string(string):
    result = ''
    char = ''
    count = ''
    s_len = len(string)

    for i in range(s_len):
        if string[i].isalpha():
            if count != '':
                result += char * (int(count) - 1)
                count = ''
            char = string[i]
            result += char
        else:
            count += string[i]
            if i == s_len-1:
                result += char * (int(count) - 1)
    return result


print(decompress_string('a40b3c2d500'))