from src.Figure import Figure
from src.Square import Square


def test_instance(create_square):
    assert isinstance(create_square, Square)


def test_inheritance(create_square):
    assert isinstance(create_square, Figure)


def test_calculate_area(create_square):
    assert create_square.calculate_area(15) == 225


def test_calculate_perimeter(create_square):
    assert create_square.calculate_perimeter(3) == 12


def test_add_area(create_square, create_rectangle):
    create_square.calculate_area(15)
    create_rectangle.calculate_area(15, 10)
    assert create_square.add_area(create_rectangle) == 300
