import copy
import numpy as np


class Point:
    @staticmethod
    def evaluate(input):
        pass

    @staticmethod
    def associate(output):
        pass

    def __init__(self, input):
        self.input = []
        self.output = []
        self.sub_space_index = -1

        self.input = np.asarray(copy.deepcopy(input))
        self.output = Point.evaluate(self.input)
        self.sub_space_index = Point.associate(self.output)
