# нахождение факториала
factorial = lambda n: n * factorial(n-1) if n > 1 else 1.
print(factorial(int(input('add number: '))))