from src.Figure import Figure
from src.Rectangle import Rectangle


def test_instance(create_rectangle):
    assert isinstance(create_rectangle, Rectangle)


def test_inheritance(create_rectangle):
    assert isinstance(create_rectangle, Figure)


def test_calculate_area(create_rectangle):
    assert create_rectangle.calculate_area(15, 10) == 75


def test_calculate_perimeter(create_rectangle):
    assert create_rectangle.calculate_perimeter(3, 4) == 14


def test_add_area(create_rectangle, create_triangle):
    create_rectangle.calculate_area(15, 10)
    create_triangle.calculate_area(15, 10)
    assert create_rectangle.add_area(create_triangle) == 150
