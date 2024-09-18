def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            if type(i) == int:
                result = result + i
            else:
                print(f'Некорректный тип данных для подсчета суммы, {i}')
                incorrect_data += 1
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    return (result, incorrect_data)
def calculate_average(numbers):
    result = personal_sum(numbers)
    if result == None:
        return None
    try:
        return result[0]/(len(numbers)-result[1])
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average('1, 2, 3')}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
