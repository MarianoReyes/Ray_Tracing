from ray import Raytracer
from sphere import Sphere
from color import color
from vector import V3
from material import Material
from light import Light

r = Raytracer(800, 800)
r.background_color = (color(255, 255, 255)).to_bytes()
r.clear()
red = Material(diffuse=color(255, 20, 20), albedo=(0.7, 0.3), spec=100)
rubber = Material(diffuse=color(80, 0, 0),  albedo=(0.9, 0.1), spec=20)
ivory = Material(diffuse=color(100, 100, 80), albedo=(0.6, 0.3), spec=50)

r.light = Light(V3(-20, 20, 20), 2, color(255, 255, 255))
r.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(-2, -1, -12), 2, rubber),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, 2, -10), 2, ivory),
]
r.render()
r.write('main.bmp')
