import pytest
from ammonite import ureg
from ammonite.Object2D import Rectangle, Square, Circle


@pytest.fixture
def rectangle():
    return Rectangle(width=2 * ureg.m, length=3 * ureg.m)


@pytest.fixture
def square():
    return Square(side=2 * ureg.m)


@pytest.fixture
def circle():
    return Circle(radius=3 * ureg.m)


def test_rectangle(rectangle):
    assert rectangle.area.check('[length]**2')
    assert rectangle.perimeter.check('[length]')
    assert rectangle.area.magnitude == pytest.approx(6)
    assert rectangle.perimeter.magnitude == pytest.approx(10)


def test_square(square):
    assert square.area.check('[length]**2')
    assert square.perimeter.check('[length]')
    assert square.area.magnitude == pytest.approx(4)
    assert square.perimeter.magnitude == pytest.approx(8)


def test_square_from_area(square):
    square = Square.from_area(4 * (ureg.meter ** 2))
    assert square.side.magnitude == pytest.approx(2)
    assert square.perimeter.magnitude == pytest.approx(8)


def test_square_from_perimeter(square):
    square = Square.from_perimeter(8 * ureg.meter)
    assert square.side.magnitude == pytest.approx(2)
    assert square.area.magnitude == pytest.approx(4)


def test_circle(circle):
    assert circle.area.check('[length]**2')
    assert circle.perimeter.check('[length]')
    assert circle.area.magnitude == pytest.approx(28.274333882)
    assert circle.perimeter.magnitude == pytest.approx(18.849555922)


def test_circle_from_diameter(circle):
    circle = Circle.from_diameter(6 * ureg.meter)
    assert circle.radius.magnitude == pytest.approx(3)
    assert circle.area.magnitude == pytest.approx(28.274333882)
    assert circle.perimeter.magnitude == pytest.approx(18.849555922)


def test_circe_from_area(square):
    circle = Circle.from_area(28.274333882 * (ureg.meter ** 2))
    assert circle.radius.magnitude == pytest.approx(3)
    assert circle.diameter.magnitude == pytest.approx(6)
    assert circle.perimeter.magnitude == pytest.approx(18.849555922)


def test_circle_from_perimeter(square):
    circle = Circle.from_perimeter(18.849555922 * ureg.meter)
    assert circle.radius.magnitude == pytest.approx(3)
    assert circle.diameter.magnitude == pytest.approx(6)
    assert circle.area.magnitude == pytest.approx(28.274333882)
