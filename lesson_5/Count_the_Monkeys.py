# You take your son to the forest to see the monkeys. You know that there are a certain number there (n),
# but your son is too young to just appreciate the full number, he has to start counting them from 1.

# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers
# up to and including that number, but excluding zero.

# For example:
# monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# monkeyCount(1) # --> [1]


def monkey_count(n):
    return list(range(1, n + 1))


num_1 = int(input("How many monkeys there: "))


def count(num):
    return [i for i in range(1, num + 1)]


def monkey(n):
    list1 = []
    l = 1
    while n > 0:
        list1.append(l)
        l += 1
        n -= 1
    return list1


print(monkey_count(num_1))


