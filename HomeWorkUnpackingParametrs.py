def print_params(a=1, b='строка', c='номер'):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, 2, True)

values_list = [1, 'one', True]
values_dict = {'a': 20, 'b': 'Welcome', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 23]
print_params(*values_list_2, 42)
