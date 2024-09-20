from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.day = 0

    day = 0
    def run(self):
        print(f'{self.name} на нас напали!\n')
        i = 100
        while i != 0:
            i -= self.power
            self.day += 1
            print(f'Рыцарь {self.name} сражается {self.day} дней!...Осталось {i} воинов')
            sleep(1)
        print(f'{self.name} одержал победу за {self.day} дней')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битва закончилась!')

