from ray import Raytracer
from sphere import Sphere
from color import color
from vector import V3
from material import Material
from light import Light
from plane import Plane
from envmap import *

r = Raytracer(800, 800)

r.light = Light(
    position=V3(-20, 10, 20),
    intensity=1.5,
    c=color(255, 255, 255)
)

ivory = Material(diffuse=color(220, 220, 200),
                 albedo=(0.6, 0.3, 0.1, 0), spec=50)
rubber = Material(diffuse=color(180, 0, 0),
                  albedo=(0.9, 0.1, 0, 0, 0), spec=10)
mirror = Material(diffuse=color(255, 255, 255),
                  albedo=(0, 10, 0.8, 0), spec=1425)
glass = Material(diffuse=color(150, 180, 200), albedo=(
    0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)

r.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(0, 0, -5), 0.5, glass),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-3, 1, -10), 2, mirror),
    Plane(V3(0, 2.2, -5), 2, 2, mirror)
]

r.envmap = Envmap('./envmap.bmp')
r.render()
r.write('main.bmp')
