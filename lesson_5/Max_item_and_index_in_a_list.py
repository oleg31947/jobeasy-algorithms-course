# Populate a list of random numbers. Find and print the max element and the index of this element


from random import randint

length = int(input(f"Enter a list length "))
array_1 = []

for i in range(length):
    item = randint(-100, 100)
    array_1.append(item)


def find_max_item_and_its_index_in_list(array):
    maximum = array[-1]
    max_index = 0
    index = 0
    while index < len(array):
        if array[index] > maximum:
            maximum = array[index]
            max_index = index
        index += 1
    return {
        "maximum": maximum,
        "max_index": max_index,
        "array": array
    }


print(find_max_item_and_its_index_in_list(array_1))
