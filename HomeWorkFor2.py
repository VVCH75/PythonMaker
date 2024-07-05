numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
is_prime = False
for i in numbers:
    if i < 2:
        continue
    if i == 2:
        primes.append(i)
    for j in range(2, i, 1):
        if i % j == 0:
            not_primes.append(i)
            is_prime = False
            break
        is_prime = True
    if is_prime == True:
        primes.append(i)

print('Список с простыми числами: ', primes)
print('Список с непростыми числами: ', not_primes)