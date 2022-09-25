from ray import Raytracer
from sphere import Sphere
from lib import color
from vector import V3

r = Raytracer(800, 800)
r.clear()
r.scene = [
    [Sphere(V3(2.8, -1, -16), 0.3), color(0, 0, 0)],
    [Sphere(V3(2.8, 1, -16), 0.3), color(0, 0, 0)],
    [Sphere(V3(2.4, 0, -16), 0.4), color(255, 128, 0)],
    [Sphere(V3(-0.2, 0, -16), 0.3), color(0, 0, 0)],
    [Sphere(V3(-1.4, 0, -16), 0.3), color(0, 0, 0)],
    [Sphere(V3(-3, 0, -16), 0.3), color(0, 0, 0)],
    [Sphere(V3(-5, 0, -16), 3), color(255, 255, 255)],
    [Sphere(V3(-0.5, 0, -16), 2), color(255, 255, 255)],
    [Sphere(V3(2.8, 0, -16), 1.5), color(255, 255, 255)]
]
r.render()
r.write('rt1.bmp')
