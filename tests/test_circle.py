from src.Figure import Figure
from src.Circle import Circle


def test_instance(create_circle):
    assert isinstance(create_circle, Circle)


def test_inheritance(create_circle):
    assert isinstance(create_circle, Figure)


def test_calculate_area(create_circle):
    assert create_circle.calculate_area(10) == 314


def test_calculate_perimeter(create_circle):
    assert create_circle.calculate_perimeter(10) == 63


def test_add_area(create_circle, create_square):
    create_circle.calculate_area(10)
    create_square.calculate_area(15)
    assert create_circle.add_area(create_square) == 539
