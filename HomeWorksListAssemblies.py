def odd(x):
    return x % 2

def sqv(x):
    return x ** 2

list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
print(list(map(sqv, filter(odd, list_))))
