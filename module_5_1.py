class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 18)
h3 = House('Домик в деревне', 2)

h1.go_to(5)
print('ЖК Эльбрус')
print()
h2.go_to(10)
print('ЖК Горский')
print()
h3.go_to(10)
print('Домик в деревне')