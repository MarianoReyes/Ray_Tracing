from ray import Raytracer
from sphere import Sphere
from color import color
from vector import V3
from material import Material
from light import Light

r = Raytracer(800, 800)
r.clear()

rubber = Material(diffuse=color(80, 0, 0),  albedo=(0.9, 0.1, 0), spec=20)
ivory = Material(diffuse=color(100, 100, 80), albedo=(0.6, 0.3, 0), spec=50)
mirror = Material(diffuse=color(255, 255, 255), albedo=(0, 1, 0.8), spec=1425)

r.light = Light(V3(-20, 20, 20), 2, color(255, 255, 255))
r.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(-2, -1, -12), 2, mirror),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, 2, -10), 2, ivory),
]
r.render()
r.write('main.bmp')
