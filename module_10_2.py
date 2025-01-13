import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self,name = str,power = int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            enemies -= self.power
            sleep(1)
            day += 1
            if enemies < 0:
                print(f'{self.name} сражается {day} дней, воинов не осталось')
            else:
                print(f"{self.name} сражается {day} день(дня).., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')






