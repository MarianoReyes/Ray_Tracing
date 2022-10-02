from ray import Raytracer
from sphere import Sphere
from color import color
from vector import V3
from material import Material
from light import Light

r = Raytracer(800, 800)
r.background_color = (color(255, 255, 255)).to_bytes()
r.clear()

black = Material(diffuse=color(0, 0, 0), albedo=(0.9, 0.1), spec=10)
brown = Material(diffuse=color(101, 67, 33), albedo=(0.6, 0.4), spec=50)
light_brown = Material(diffuse=color(200, 170, 130), albedo=(1, 0), spec=10)
white = Material(diffuse=color(255, 255, 255), albedo=(0.9, 0.1), spec=10)
red = Material(diffuse=color(255, 20, 20), albedo=(0.7, 0.3), spec=100)
rubber = Material(diffuse=color(80, 0, 0),  albedo=(0.9, 0.1), spec=20)
ivory = Material(diffuse=color(100, 100, 80), albedo=(0.6, 0.3), spec=50)

r.light = Light(V3(-5, -5, 0), 1, color(255, 255, 255))
# osito
r.scene = [
    # cuerpo
    Sphere(V3(0, 2, -16), 3, red),
    Sphere(V3(3.2, 0, -14), 1.5, light_brown),
    Sphere(V3(-3.2, 0, -14), 1.5, light_brown),
    Sphere(V3(2.8, 4.3, -14), 1.5, light_brown),
    Sphere(V3(-2.8, 4.3, -14), 1.5, light_brown),
    # cabeza
    Sphere(V3(0, -2.7, -14), 2, light_brown),
    Sphere(V3(0, -1.8, -12), 1, brown),
    # orejas
    Sphere(V3(2, -3.4, -12), 0.6, brown),
    Sphere(V3(-2, -3.4, -12), 0.6, brown),
    # ojos
    Sphere(V3(0.7, -3.1, -12), 0.3, black),
    Sphere(V3(-0.7, -3.1, -12), 0.3, black),
    Sphere(V3(0, -1.8, -10), 0.3, black),
]
r.render()
r.write('rt2.bmp')
