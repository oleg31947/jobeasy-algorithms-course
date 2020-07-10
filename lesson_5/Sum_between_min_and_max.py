# Find a sum of elements between min and max elements. Min and max elements are not included


def sum_between_min_and_max(array):
    maximum = array[0]
    minimum = array[0]
    max_index = 0
    min_index = 0
    index = 0
    while index < len(array):
        if array[index] > maximum:
            maximum = array[index]
            max_index = index
        if array[index] < minimum:
            minimum = array[index]
            min_index = index
        index += 1
    if max_index < min_index:
        subarray = array[max_index + 1:min_index]
    else:
        subarray = array[min_index + 1:max_index]
    result = sum(subarray)
    return {
        "min": minimum,
        "max": maximum,
        "subarray": subarray,
        "result": result
    }


print(sum_between_min_and_max([1]))
