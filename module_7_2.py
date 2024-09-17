import io
strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
strings_positions = {}
def custom_write(file_name, strings):
    file = open(file_name, 'w')
    for elem in strings:
        file.write(elem.encode('utf-8').decode('utf-8') + '\n')
    file.close()

result = custom_write('test.txt', strings)
with open('test.txt', 'r') as r_file:
    line_num = 0
    while True:
        line_num += 1
        key = (line_num, r_file.tell())
        line = r_file.readline()
        if not line:
            break
        strings_positions[key] = line.rstrip('\n')
        print((key, strings_positions[key]))
