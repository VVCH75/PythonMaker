from time import sleep
from datetime import datetime
from threading import Thread
def wite_words(word_count, file_name):
    my_file = open(file_name, 'w+')
    my_file.write(str(word_count))
    my_file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
wite_words(10, 'example1.txt')
sleep(0.1)
wite_words(30, 'example2.txt')
sleep(0.1)
wite_words(200, 'example3.txt')
sleep(0.1)
wite_words(100, 'example4.txt')
sleep(0.1)
time_end = datetime.now()
time_res = time_end - time_start
print(f'На запись во все файлы потребовалось {time_res}\n')


time_start = datetime.now()
trd_1 = Thread(target=wite_words(10, 'example5.txt'))
trd_2 = Thread(target=wite_words(30, 'example6.txt'))
trd_3 = Thread(target=wite_words(200, 'example7.txt'))
trd_4 = Thread(target=wite_words(100, 'example8.txt'))

trd_1.start()
trd_2.start()
trd_3.start()
trd_4.start()

trd_1.join()
trd_2.join()
trd_3.join()
trd_4.join()


time_end = datetime.now()
time_res = time_end - time_start
print(f'На обработку всех потоков потребовалось {time_res}')
