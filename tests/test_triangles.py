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
