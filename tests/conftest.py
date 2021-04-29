import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def create_triangle():
    return Triangle("triangle", 3)


@pytest.fixture()
def create_circle():
    return Circle("circle", 0)


@pytest.fixture()
def create_rectangle():
    return Rectangle("rectangle", 4)


@pytest.fixture()
def create_square():
    return Square("square", 0)
