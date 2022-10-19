from intersect import *
from vector import V3
from plane import *


class Cube(object):
    def __init__(self, center, size, material):
        self.center = center
        self.size = size
        self.material = material

        # caras x
        self.left = PlaneX(
            V3(center[0]-size/2, center[1], center[2]), size, size, material, -1)
        self.right = PlaneX(
            V3(center[0]+size/2, center[1], center[2]), size, size, material, 1)

        # caras y
        self.up = PlaneY(
            V3(center[0], center[1]+size/2, center[2]), size, size, material, 1)
        self.down = PlaneY(
            V3(center[0], center[1]-size/2, center[2]), size, size, material, -1)

        # solo cara frontal para minimizar consumo de recursos
        self.front = PlaneZ(
            V3(center[0], center[1], center[2]+size/2), size, size, material, 1)

    def ray_intersect(self, origin, direction):

        izquierda = self.left.ray_intersect(origin, direction)
        derecha = self.right.ray_intersect(origin, direction)
        arriba = self.up.ray_intersect(origin, direction)
        abajo = self.down.ray_intersect(origin, direction)
        frente = self.front.ray_intersect(origin, direction)

        interseccion = [izquierda, derecha, arriba, abajo, frente]

        menor = 99999
        point = 0
        for i in range(len(interseccion)):
            if interseccion[i] and interseccion[i].distance < menor:
                menor = interseccion[i].distance
                point = interseccion[i]

        return point
