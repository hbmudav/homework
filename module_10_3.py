import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance: int = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            incr = randint(50, 500)
            self.balance += incr
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {incr}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            decr = randint(50, 500)
            print(f'Запрос на снятие {decr} рублей')
            if self.balance <= decr:
                self.balance -= decr
            print(f'Снятие: {decr}. Баланс: {self.balance}')
            if decr > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
