# You have a list of countries and their cities. After that a list of cities is input.
# For every city indicate what country it is in.

# Input
# [
#   ['USA', 'Dallas', 'Washington', 'Los-Angeles', 'San-Francisco'],
#   ['Canada', 'Ottawa', 'Vancouver', 'Montreal']
# ]
# ['Montreal', 'Washington', 'Dallas']


# Output
# ['Canada', 'USA', 'USA']


def countries_and_cities(data, needed_cities):
    dictionary = {}
    for item in data:
        index = 1
        while index < len(item):
            dictionary[item[index]] = item[0]
            index += 1
    return dictionary
    # result = []
    # for needed_city in needed_cities:
    #     if needed_city in dictionary:
    #         result.append(dictionary[needed_city])
    #     else:
    #         result.append(f'{needed_city} not in our list of cities')
    # return result


print(countries_and_cities([
   ['USA', 'Dallas', 'Washington', 'Los-Angeles', 'San-Francisco'],
   ['Canada', 'Ottawa', 'Vancouver', 'Montreal'],
   ['Russia', 'Moscow', 'Novosibirsk', 'Vladivostok', 'Tula']
], ['Montreal', 'Washington', 'Dallas', 'Omsk', 'Tula'])
)