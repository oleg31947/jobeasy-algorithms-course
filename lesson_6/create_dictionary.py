# There are two lists that have different length. First has keys and the second has values.
# Create a function, which creates a dictionary of keys and values.
# If the is not enough values to match each key, this key should have value equal to None.
# If the is not enough keys to match each value, this value should be ignored.


names = [
    'Aliza Hulme',
    'Isaiah Mcgill',
    'Keiran Partridge',
    'Michele Wilcox',
    'Jordon Rocha',
    'Shakir Calhoun',
    'Lexi Bob',
    'Nimrah Regan',
    'Scarlet Roberts',
    'Emily-Jane Mejia'
]
jobs = [
    'Speech therapist',
    'Animal breeder',
    'Miner',
    'IT consultant',
    'Butler',
    'Radio presenter',
    'Architect',
    'Police officer',
    '2',
    '3',
    '4'
]


def create_dictionary(keys, values):
    result = {}
    index = 0
    while index < len(keys):
        if index < len(values):
            result[keys[index]] = values[index]
        else:
            result[keys[index]] = None
        index += 1
    return result


print(create_dictionary(names, jobs))