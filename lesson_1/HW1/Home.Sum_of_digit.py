# TODO: Домашнее задание: Написать программу для числа из любого количества цифр.
#  Вместо числа из 3 цифр, нужно считать сумму числа из n цифр.
#  Где  n вводит пользователь с клавиатуры. Только положительные.

from random import randint

digits = int(input("Ввести порядок числа: "))
def sum_of_digit(digits):
    if digits < 1:
        print('Неверное значение. Число должно быть больше или равно 1')
        quit()
    down = 1 * 10 ** (digits - 1)
    up = (1 * 10 ** digits) - 1
    n = randint(down, up)
    print(f'мы получили число {n}')
    result = 0
    i = 0
    while i < digits:
        result += n % 10
        n = n // 10
        i += 1

    print(f'результат {result}')


sum_of_digit(digits)
# Сложность O(N)
