def test_func(*params):
    print(*params)
test_func(1, True, 'все типы здесь')

def factorial(n):
    if n == 1:
         return 1
    else:
         return n * factorial(n - 1)
print(factorial(5))