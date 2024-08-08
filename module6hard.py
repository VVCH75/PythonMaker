from math import pi

class Figure:
    sides_count = 0
    def __init__(self, __color, __sides):
        self.__color = __color
        self.__sides = __sides
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *args):
        for i in args:
            if i >= 0 and i <= 255:
                return True
            break
        return False


    def set_color(self, *args):
        if self.__is_valid_color(*args) == True:
            self.__color = [*args]
        else:
            self.__color = [*self.__color]

    def __is_valid_sides(self):
        if self.__sides == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        side = 0
        if isinstance(self, Circle):
            side = int(*self.__sides)
            return side
        elif isinstance(self, Cube):
            for i in self.__sides:
                side += i
            return side
        elif isinstance(self, Triangle):
            for i in self.__sides:
                side += i
            return side

    def set_sides(self, *new_sides):
        LL = []
        if self.sides_count == len(new_sides):
            self.__sides = [*new_sides]
        else:
            for i in range(self.sides_count):
                LL.append(self.__sides)
            self.__sides = LL


class Circle(Figure):
    sides_count = 1
    def __radius(self):
        ss = self.get_sides()
        return ss / (pi * 2)

    def get_square(self):
        sq = self.__radius()
        return pi * sq ** 2

class Triangle(Figure):
    sides_count = 3

    def __height(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = (a + b + c) / 2
        Ha = (p * (p - a) * (p - b) * (p - c)) ** 0.5 / a
        Hb = (p * (p - a) * (p - b) * (p - c)) ** 0.5 / b
        Hc = (p * (p - a) * (p - b) * (p - c)) ** 0.5 / c
        return Ha, Hb, Hc

    def get_square(self):
        St = self.__height()[0]
        return self.get_sides()[0] * St / 2
class Cube(Figure):
    sides_count = 12
    __sides = 12
    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())