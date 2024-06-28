# Фабрика функций

def fabric_function(action):
    if action == 'add':
        def function(x, y):
            return x + y
    elif action == 'sub':
        def function(x, y):
            return x - y
    elif action == 'mult':
        def function(x, y):
            return x * y
    else:
        def function(x, y):
            return x / y
    return function

act1 = fabric_function('add')
act2 = fabric_function('sub')
act3 = fabric_function('mult')
act4 = fabric_function('div')
print(act1(1,2))
print(act2(1,2))
print(act3(1,2))
print(act4(1,2))

# Лямбда функция
my_func = lambda x: x ** 2
print(my_func(4))

def kvadrat(x):
    return x **2
print(kvadrat(4))

# Вызываемые объекты

class Rect:
    def __init__(self, a):
        self.a = a
    def __call__(self, b):
        print('Стороны:', self.a, 'и', b)
        return self.a * b
side_a = Rect(a=2)
sqv = side_a(b=4)

print('Площадь:', sqv)