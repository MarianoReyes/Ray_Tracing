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
    PlaneY(V3(0, 2, -4), 10, 10, grass, -1),

    # fila 3
    Cube((-2, -1, -5), 1, leaves),
    Cube((0, -1, -5), 1, leaves),
    Cube((-1, -1, -6), 1, leaves),
    Cube((-1, -1, -4), 1, leaves),
    Cube((-1, -2, -5), 1, leaves),
    Cube((-1, 0, -5), 1, logg),
    Cube((-1, 1, -5), 1, logg),
]

r.envmap = Envmap('./envmap.bmp')
r.render()
r.write('escena_final.bmp')
