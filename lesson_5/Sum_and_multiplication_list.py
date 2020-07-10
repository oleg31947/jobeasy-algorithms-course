# Enter elements from a keyboard. Calculate sum and multiplication of elements.
# Print the list, calculated sum, and multiplication of elements

length = int(input(f"Enter a length of a list "))
array_1 = []

for item in range(length):
    number = int(input(f"Enter a value of element "))
    array_1.append(number)


def sum_and_mult(array):
    summ = 0
    mult = 1
    for item in array:
        summ += item
        mult *= item
    return {
        "summ": summ,
        "mult": mult,
        "array": array
    }


print(sum_and_mult(array_1))
