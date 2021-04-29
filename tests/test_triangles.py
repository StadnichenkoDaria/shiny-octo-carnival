# Написать тесты с использованием pytest на эти классы.
# По одному тесту на каждый метод каждой фигуры.
# Т.е. будет четыре тестовых модуля по 5 тестов на каждый. Можно написать и больше. :)

# Тесты: Класс Треугольник
# 1. Проверить, что созданный объект является экз класс Фигур
# 2. Проверить, что площадь считается верно
# 3. Проверить, что периметр считается верно
# 4. Проверить, что сумма площадей считается верно

from src.Figure import Figure
from src.Triangle import Triangle


def test_instance(create_triangle):
    assert isinstance(create_triangle, Triangle)


def test_inheritance(create_triangle):
    assert isinstance(create_triangle, Figure)


def test_calculate_area(create_triangle):
    assert create_triangle.calculate_area(15, 10) == 75.0


def test_calculate_perimeter(create_triangle):
    assert create_triangle.calculate_perimeter(3, 4, 2) == 9


def test_add_area(create_triangle, create_circle):
    create_triangle.calculate_area(15, 10)
    create_circle.calculate_area(10)
    assert create_triangle.add_area(create_circle) == 389
