from vector import *
from intersect import *

# clase principal creada por dennis


class Plane(object):
    def __init__(self, center, w, l, material):
        self.center = center
        self.w = w
        self.l = l
        self.material = material

    def ray_intersect(self, origin, direction):
        # nueva magia

        # cara de arriba
        d = -(origin.y + self.center.y) / direction.y
        impact = (direction * d) - origin
        normal = V3(0, 1, 0)

        if d <= 0 or \
                impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) or \
                impact.z > (self.center.z + self.l/2) or impact.z < (self.center.z - self.l/2):
            return None

        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )

# clases dependiendo de donde se quiera el plano


class PlaneZ(object):
    def __init__(self, center, width, height, material, normal):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
        self.normal = V3(0, 0, normal)
        self.xmin = center.x-width*0.5
        self.ymin = center.y-height*0.5

    def ray_intersect(self, origin, direction):

        d = (self.center.z - origin.z) / direction.z
        impact = direction * d - origin

        if d <= 0 or \
                impact.x > (self.center.x + self.width/2) or impact.x < (self.center.x - self.width/2) or \
                impact.y > (self.center.y + self.height/2) or impact.y < (self.center.y - self.height/2):

            return None

        return Intersect(
            distance=d,
            point=impact,
            normal=self.normal,
            percentage=((impact.x - self.xmin)/self.width,
                        (impact.y - self.ymin)/self.height)
        )


class PlaneY(object):
    def __init__(self, center, width, height, material, normal):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
        self.normal = V3(0, normal, 0)
        self.xmin = center.x-width*0.5
        self.ymin = center.z-width*0.5

    def ray_intersect(self, origin, direction):

        d = (self.center.y - origin.y) / direction.y
        impact = direction * d - origin

        if d <= 0 or \
                impact.x > (self.center.x + self.width*0.5) or impact.x < (self.center.x - self.width*0.5) or \
                impact.z > (self.center.z + self.height*0.5) or impact.z < (self.center.z - self.height*0.5):

            return None

        return Intersect(
            distance=d,
            point=impact,
            normal=self.normal,
            percentage=((impact.x - self.xmin)/self.width,
                        (impact.z - self.ymin)/self.height)
        )


class PlaneX(object):
    def __init__(self, center, width, height, material, normal):
        self.center = center
        self.width = width
        self.height = height
        self.material = material
        self.normal = V3(normal, 0, 0)
        self.xmin = center.z-width*0.5
        self.ymin = center.y-width*0.5

    def ray_intersect(self, origin, direction):

        d = (self.center.x - origin.x) / direction.x
        impact = direction * d - origin

        if d <= 0 or \
                impact.y > (self.center.y + self.width*0.5) or impact.y < (self.center.y - self.width*0.5) or \
                impact.z > (self.center.z + self.height*0.5) or impact.z < (self.center.z - self.height*0.5):

            return None

        return Intersect(
            distance=d,
            point=impact,
            normal=self.normal,
            percentage=((impact.z - self.xmin)/self.height,
                        (impact.y - self.ymin)/self.width)
        )
