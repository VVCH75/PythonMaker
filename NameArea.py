def inner_function(args):
    print(args)
    def test_function(args):
        inner_function('Я в области видимости функции test_function')

inner_function('Я вне области видимости функции test_function')
