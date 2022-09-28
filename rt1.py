from ray import Raytracer
from sphere import Sphere
from lib import color
from vector import V3
from material import Material
from light import Light

r = Raytracer(800, 800)
r.clear()

black = Material(diffuse=color(0, 0, 0))
white = Material(diffuse=color(255, 255, 255))
orange = Material(diffuse=color(255, 128, 0))

r.light = Light(V3(0, 0, 0), 1)
r.scene = [
    Sphere(V3(-5, 0, -16), 3, white),
    Sphere(V3(-0.5, 0, -16), 2, white),
    Sphere(V3(2.8, 0, -16), 1.5, white),
    Sphere(V3(2, -0.5, -11), 0.1, black),
    Sphere(V3(2, 0.5, -11), 0.1, black),
    Sphere(V3(1.898, 0, -12), 0.2, orange),
    Sphere(V3(-0.2, 0, -11), 0.1, black),
    Sphere(V3(-1.4, 0, -11), 0.1, black),
    Sphere(V3(-3, 0, -11), 0.1, black)
]
r.render()
r.write('rt1.bmp')
