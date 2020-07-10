# You have a list of numbers. You should sum up all numbers and output their sum.

array_1 = [2, 4, 6]


def summ(array: list):
    if len(array) == 1:
        return array[0]
    else:
        value = array[0:1]
        array = array[1:]
        return value[0] + summ(array)


print(summ(array_1))
