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

    def render(self):
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
                    V3(0, 0, 0), direction, color_actual)

    def cast_ray(self, origin, direction, color_actual):
        # la magia pasa
        for esfera in self.scene:
            intersect = esfera[0].ray_intersect(origin, direction)
            if intersect:
                return esfera[1]

        return color_actual
