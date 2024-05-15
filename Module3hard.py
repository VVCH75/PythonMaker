s = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*data_structure):
    global s
    for i in data_structure:
        if isinstance(i, int):
            s += i
        elif isinstance(i, str):
            s += len(i)
        elif isinstance(i, list):
            calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            calculate_structure_sum(*i)
        elif isinstance(i, set):
            calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                calculate_structure_sum(key)
                calculate_structure_sum(value)
    return s

result = calculate_structure_sum(data_structure)
print(result)
