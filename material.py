import struct
from color import *


class Material:
    def __init__(self, diffuse=color(255, 255, 255), albedo=(1, 0, 0, 0), spec=0, refractive_index=0, texture=None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.texture = texture


class Texture:

    def __init__(self, path):
        self.path = path
        self.width = 0
        self.heigth = 0
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(10)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(18)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.heigth = struct.unpack("=l", image.read(4))[0]
            image.seek(header_size)
            self.pixels = []

            for y in range(self.heigth):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))

                    self.pixels[y].append(color(r, g, b))

    def get_color(self, tx, ty):
        x = round(tx*self.width)
        y = round(ty*self.heigth)

        return self.pixels[y][x]

    def intensity(self, tx, ty, intensity):
        x = round(tx*(self.width-1))
        y = round(ty*(self.heigth-1))

        b = round(self.pixels[y][x][0]*intensity)
        g = round(self.pixels[y][x][1]*intensity)
        r = round(self.pixels[y][x][2]*intensity)

        b = max(0, min(b, 255))
        g = max(0, min(g, 255))
        r = max(0, min(r, 255))

        return color(b, g, r)
