import math
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in [r,g,b]:
            if isinstance(i, int) and 0 <= i <= 255:
                return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r,g,b) == True:
            self.__color = [r,g,b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if isinstance(side, int) and side > 0:
                    return True
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides, filled)
        self.__sides = __sides[0]
        __radius = self.__sides / (2 * math.pi)

    def get_square(self, __radius):
        Sc = math.pi * (self.__radius ** 2)
        return Sc

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides)

    def get_square(self, __sides):
        self.__len__(__sides)
        p = self.summa * 0.5
        St = (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5
        return St

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=True):
        if len(__sides) == 1:
            __sides = [__sides[0]] * self.sides_count
        super().__init__(__color, *__sides)

    def get_volume(self, *__sides):
        V = self.get_sides()[0] ** 3
        return V


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
print()
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
print()
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
