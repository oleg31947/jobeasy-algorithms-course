# User enters a string and a number. Write a recursive function, which will print your string n-times.

string1 = input('Enter a string: ')
number = int(input('Enter a number: '))


def recursive_replication(string, n):
    if n > 1:
        return recursive_replication(string, n - 1) + string
    elif n == 1:
        return string
    else:
        print('asdas!')


print(recursive_replication(string1, number))
