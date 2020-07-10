# Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day.
# Go through a list of children, and return a list containing every child who appeared on Santa's list.
# Do not add any child more than once.


def find_children(santas_list, children):
    result = []
    for child in santas_list:
        if child in children:
            result.append(child)
    return result


print(find_children(['sam', 'john', 'danny', 'ilya', 'rose'], ['adolf', 'sam', 'bob', 'ilya', 'rose', 'stan', 'andrei']))
