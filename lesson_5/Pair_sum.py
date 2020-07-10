# Function has given a list of integer numbers and k integer number.
# It returns all pairs of numbers from the list which equal to k.
# E.g. pair_sum([1, 3, 4, 6, 8, 2, 2], 4) returns (1,3) and (2,2)


def pair_sum(arr, k):
    result = []
    index_1 = 0
    while index_1 < len(arr):
        index_2 = 0
        while index_2 < len(arr):
            if arr[index_1] + arr[index_2] == k and index_1 != index_2:
                find = tuple(sorted((arr[index_1], arr[index_2])))
                if find not in result:
                    result.append(find)
            index_2 += 1
        index_1 += 1
    return result


print(pair_sum([1, 3, 4, 6, 8, 2, 2], 4))
