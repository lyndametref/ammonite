# Ammonite: Geometry calculation cheatsheet

Unit aware calculation of geometrical primitives' area, volumes, etc. It 
is base on [pint](https://pint.readthedocs.io/en/stable/) for a seamless unit management and easy conversion.

This package is at an early stage of development, it currently only include 
    
  - 3D:
       - Box
       - Cube
       - Sphere

  - 2D:
       - Rectangle
       - Square
       - Circle


## Usage

```python
from ammonite import ureg
from ammonite.Object3D import Sphere

my_sphere = Sphere(radius=3 * ureg.meter)
print(my_sphere.volume)
# 113.09733552923254 meter ** 3
print(my_sphere.area)
# 113.09733552923255 meter ** 2

```

## Contributions

Any comments to report a bug, improve this package, make it follow best practices which I might not know of or improve 
its  automation are welcome.



            

