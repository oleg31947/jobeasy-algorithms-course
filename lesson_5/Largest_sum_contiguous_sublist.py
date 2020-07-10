# In a list find continuous sublist which has the greater sum of elements


def largest_sum_contiguous_sublist(array):
    best_sum = 0
    best_sublist = []
    index_1 = 0
    while index_1 < len(array):
        index_2 = index_1 + 1
        current_sum = array[index_1]
        sublist = [array[index_1]]
        while index_2 < len(array):
            current_sum += array[index_2]
            sublist.append(array[index_2])
            if current_sum > best_sum:
                best_sum = current_sum
                best_sublist = sublist.copy()
            index_2 += 1
        index_1 += 1
    return {
        "best_sum": best_sum,
        "best_sublist": best_sublist
    }


print(largest_sum_contiguous_sublist([-99, 5, 3, -200, 2, 8]))
