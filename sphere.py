class Sphere(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def ray_intersect(self, origin, direction):
        L = self.center - origin
        tca = L @ direction
        l = L.length()

        d2 = l**2 - tca**2

        # si no pasa por la esfera
        if d2 > self.radius**2:
            return False

        thc = (self.radius**2 - d2) ** 0.5

        # puntos que chocan con esfera
        t0 = tca - thc
        t1 = tca + thc

        # si esta adentro del circulo
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return False

        return True
