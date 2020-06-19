# Посчитать четные и нечетные цифры числа. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


n = int(input(f"Введите число: "))


def count_odd_even(n):
    odd_count = 0
    even_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n = n // 10
    print(f"Нечетых цифр в числе {odd_count}")
    print(f"Четых цифр в числе {even_count}")


count_odd_even(n)

# Сложность O(N)
