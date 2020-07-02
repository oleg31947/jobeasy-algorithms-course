
def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return recursion_factorial(n - 1) * n


print(recursion_factorial(7))
