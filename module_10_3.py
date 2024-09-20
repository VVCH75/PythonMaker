from threading import Thread, Lock
from time import sleep
from random import randint

class Bank(Thread):
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(101):
            random_num = randint(50, 500)
            self.balance += random_num
            print(f'Пополнение: {random_num}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.01)



    def take(self):
        for i in range(101):
            random_num = randint(50, 500)
            print(f'Запрос на {random_num}')
            if self.balance >= random_num:
                self.balance -= random_num
                print(f'Снятие {random_num}. Текущий баланс {self.balance}')
            else:
                self.lock.acquire()
                i -= 1
                print(f'Запрос отклонён, недостаточно средств')

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

