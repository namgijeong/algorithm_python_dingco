def factorial(n):
    if n == 1:
        return 1
    multiply = n * factorial(n-1)
    return multiply


print(factorial(5))