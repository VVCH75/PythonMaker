def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 2:
            print(f'Число {n} ни составное ни простое')
            return n
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                print(f'Число {n} составное')
                return n
        print(f'Число {n} простое')
        return n
    return wrapper


@is_prime
def sum_three(*args):
    summa = 0
    for num in args:
        if not str(num).isdigit():
            return
        else:
            summa += int(num)
    return summa

result = sum_three(2, 3, 6)
print(result)