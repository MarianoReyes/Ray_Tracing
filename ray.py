from lib import *
from math import *
from vector import V3
from sphere import Sphere


class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.background_color = color(178, 255, 255)
        self.current_color = color(255, 255, 255)
        self.clear()
        self.scene = []

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def point(self, x, y, c=None):
        if y >= 0 and self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c or self.current_color

    def write(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)

    def render(self, number, color):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)

        for y in range(self.height):
            for x in range(self.width):
                color_actual = self.framebuffer[y][x]
                i = (2*(x + 0.5)/self.width - 1) * ar * tana
                j = -(2*(y + 0.5)/self.height - 1) * tana
                direction = V3(i, j, -1).norm()
                self.framebuffer[y][x] = self.cast_ray(
                    V3(0, 0, 0), direction, number, color_actual, color)

    def cast_ray(self, origin, direction, i, color_actual, color_deseado):
        # la magia pasa
        intersect = self.scene[i].ray_intersect(origin, direction)
        if intersect:
            return color_deseado
        else:
            return color_actual


r = Raytracer(800, 800)
r.scene = [
    Sphere(V3(-5, 0, -16), 3),
    Sphere(V3(-0.5, 0, -16), 2),
    Sphere(V3(2.8, 0, -16), 1.5),
    Sphere(V3(2.8, -1, -16), 0.3),
    Sphere(V3(2.8, 1, -16), 0.3),
    Sphere(V3(2.4, 0, -16), 0.4),
    Sphere(V3(-0.2, 0, -16), 0.3),
    Sphere(V3(-1.4, 0, -16), 0.3),
    Sphere(V3(-3, 0, -16), 0.3),
]
r.render(0, color(255, 255, 255))
r.render(1, color(255, 255, 255))
r.render(2, color(255, 255, 255))
r.render(3, color(0, 0, 0))
r.render(4, color(0, 0, 0))
r.render(5, color(255, 128, 0))
r.render(6, color(0, 0, 0))
r.render(7, color(0, 0, 0))
r.render(8, color(0, 0, 0))
r.write('r.bmp')
