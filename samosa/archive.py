import numpy as np

from point import Point


class Archive:
    def __init__(self):
        self.points = np.asarray([], dtype=Point)

    def size(self):
        return self.points.size

    def add(self, point):
        self.points = np.append(self.points, [point])
