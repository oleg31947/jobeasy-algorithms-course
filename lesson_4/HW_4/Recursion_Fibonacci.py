
def recursion_fibonacci(n):
    if n <= 2:
        return 1
    else:
        return recursion_fibonacci(n - 1) + recursion_fibonacci(n - 2)


print(recursion_fibonacci(6))
