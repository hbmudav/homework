from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
         sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queve = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    break

            else:
                self.queve.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queve.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queve.empty():
                        next_guest = self.queve.get()
                        table.guest = next_guest
                        print(f'{next_guest.name} вышел(ла) из очереди и сел(а) за стол номер {table.number}')
                        next_guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()