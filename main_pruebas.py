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
    #Sphere(V3(0, -1.5, -10), 1.5, ivory),
    #Sphere(V3(0, 0, -5), 0.5, glass),
    #Sphere(V3(1, 1, -8), 1.7, rubber),
    #Sphere(V3(-3, 1, -10), 2, mirror),
    PlaneY(V3(0, 1.5, -4), 10, 10, grass, -1),
    Cube((-1, 1.2, -5), 1, log),
]

#r.envmap = Envmap('./envmap.bmp')
r.render()
r.write('main2.bmp')
