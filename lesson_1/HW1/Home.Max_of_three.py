# Найти максимальное число из трех. Вводятся три целых числа. Определить какое из них наибольшее.


num1 = int(input(f"Первое число "))
num2 = int(input(f"Второе число "))
num3 = int(input(f"Третее число "))

def max_of_three(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(f"Наибольшее из чисел {num1},{num2},{num3} это {num1}")
        else:
            print(f"Наибольшее из чисел {num1},{num2},{num3} это {num3}")
    else:
        if num2 > num3:
            print(f"Наибольшее из чисел {num1},{num2},{num3} это {num2}")
        else:
            print(f"Наибольшее из чисел {num1},{num2},{num3} это {num3}")

max_of_three(num1, num2, num3)


# Сложность O(1)
