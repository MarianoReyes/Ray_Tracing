class Intersect(object):
    def __init__(self, distance, point, normal, percentage=(-1, -1)):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.percentage = percentage
