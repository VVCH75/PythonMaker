first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    print('Все введенные числа равны')
elif first == second or second == third or first == third:
    print('Среди введенных чисел есть два одинаковых числа')
else:
    print('Все введенные числа не равны друг другу')