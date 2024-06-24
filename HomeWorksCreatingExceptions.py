class LenError(Exception):
    pass
class StringError(Exception):
    pass
def LL(a):
    if len(a) > 1:
        raise LenError(f'Лошара, просили только одну цифру ---> {a}')
    if a.isdigit():
        return a
    else:
        raise StringError(f'Вот олень, просили же одну цифру ---> {a}')


a = input('Введите одну цифру: ')
print(LL(a))

