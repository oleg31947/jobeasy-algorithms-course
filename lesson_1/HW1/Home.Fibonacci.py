# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# По данному числу n выведите на экран указаный элемент последовательности

# Формула:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


n = int(input("Элемент ряда Фибоначчи: "))


def fibonacci(n):
    fibonacci1 = 1
    if n < 1:
        print(f'Неверное значение')
        quit()
    elif n == 1 or n == 2:
        print(fibonacci1)
    else:
        fibonacci2 = 1
        i = 0
        while i < n - 2:
            fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
            i = i + 1
            if i == n - 2:
                print(fibonacci2)


fibonacci(n)

# Сложность O(N)