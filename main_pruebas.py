from ray import Raytracer
from sphere import Sphere
from color import color
from vector import V3
from material import Material
from light import Light
from plane import *
from cube import Cube
from envmap import *
from materials import *

r = Raytracer(800, 800)

r.light = Light(
    position=V3(20, -30, 20),
    intensity=1.5,
    c=color(255, 255, 255)
)

r.scene = [
    #PlaneY(V3(0, 1.5, -4), 10, 10, grass, -1),
    # fila 3
    Cube((-1, 1, -5), 1, logg),
    Cube((-3, 2, -5), 1, grass),
    Cube((-2, 2, -5), 1, grass),
    Cube((-1, 2, -5), 1, grass),
    Cube((0, 2, -5), 1, grass),
    Cube((1, 2, -5), 1, grass),
    Cube((2, 2, -5), 1, grass),
    Cube((3, 2, -5), 1, grass),
    # fila 2
    Cube((-3, 2, -4), 1, grass),
    Cube((-2, 2, -4), 1, grass),
    Cube((-1, 2, -4), 1, grass),
    Cube((0, 2, -4), 1, grass),
    Cube((1, 2, -4), 1, grass),
    Cube((2, 2, -4), 1, grass),
    Cube((3, 2, -4), 1, grass),
    # fila 1
    Cube((-3, 2, -3), 1, grass),
    Cube((-2, 2, -3), 1, grass),
    Cube((-1, 2, -3), 1, grass),
    Cube((0, 2, -3), 1, grass),
    Cube((1, 2, -3), 1, grass),
    Cube((2, 2, -3), 1, grass2),
    Cube((3, 2, -3), 1, grass),
]

#r.envmap = Envmap('./envmap.bmp')
r.render()
r.write('main2.bmp')
