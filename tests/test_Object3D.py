import pytest
from ammonite import ureg
from ammonite.Object3D import Sphere, Box, Cube


@pytest.fixture
def box():
    return Box(2 * ureg.m, 3 * ureg.m, 4 * ureg.m)


@pytest.fixture
def cube():
    return Cube(side=2 * ureg.m)


@pytest.fixture
def sphere():
    return Sphere(radius=2 * ureg.m)


def test_box(box):
    assert box.volume.check('[length]**3')
    assert box.area.check('[length]**2')
    assert box.volume.magnitude == pytest.approx(24)
    assert box.area.magnitude == pytest.approx(52)


def test_cube(cube):
    assert cube.volume.check('[length]**3')
    assert cube.area.check('[length]**2')
    assert cube.volume.magnitude == pytest.approx(8)
    assert cube.area.magnitude == pytest.approx(24)


def test_cube_from_volume():
    cube = Cube.from_volume(volume=8 * ureg.meter**3)
    assert cube.side.magnitude == pytest.approx(2)
    assert cube.area.magnitude == pytest.approx(24)


def test_cube_from_area():
    cube = Cube.from_area(area=24 * ureg.meter**2)
    assert cube.side.magnitude == pytest.approx(2)
    assert cube.volume.magnitude == pytest.approx(8)


def test_sphere(sphere):
    assert sphere.volume.check('[length]**3')
    assert sphere.area.check('[length]**2')
    assert sphere.diameter.magnitude == pytest.approx(4)
    assert sphere.volume.magnitude == pytest.approx(33.51032)
    assert sphere.area.magnitude == pytest.approx(50.26548)


def test_sphere_from_diameter():
    sphere = Sphere.from_diameter(diameter=4 * ureg.m)
    assert sphere.radius.magnitude == pytest.approx(2)
    assert sphere.volume.magnitude == pytest.approx(33.51032)
    assert sphere.area.magnitude == pytest.approx(50.26548)


def test_sphere_from_volume():
    sphere = Sphere.from_volume(volume=33.51032 * ureg.m ** 3)
    assert sphere.area.magnitude == pytest.approx(50.26548)
    assert sphere.radius.magnitude == pytest.approx(2)
    assert sphere.diameter.magnitude == pytest.approx(4)


def test_sphere_from_area():
    sphere = Sphere.from_area(area=50.26548 * ureg.m ** 2)
    assert sphere.volume.magnitude == pytest.approx(33.51032)
    assert sphere.radius.magnitude == pytest.approx(2)
    assert sphere.diameter.magnitude == pytest.approx(4)
