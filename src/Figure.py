# Создать базовый класс геометрической фигуры (Figure).
# Реализовать на его основе классы геометрических фигур
# Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).

# Каждая фигура должна иметь атрибуты:
# name - название фигуры,
# area (вычисляемое!) - площадь,
# angles - количество углов
# perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности)

# Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур.
# Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую
# геометрическую фигуру и возвращать сумму площадей этих фигур. Если передана не геометрическая фигура,
# то нужно выдавать ошибку и сообщать что передан неправильный класс.

# Опционально (не обязательно): Запретить создавать инстансы базового класса Figure.
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name, angles):
        self.name = name,
        self.angles = angles,
        self.area = 0
        self.perimeter = 0

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            amount_area = figure.area + self.area
            return amount_area
        print("It's not figure")



