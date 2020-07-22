import copy
import numpy as np


class Point:
    @staticmethod
    def associate(output):
        pass

    def __init__(self, input, evaluate=None):
        if evaluate == None:
            try:
                Point.evaluate(input)
            except AttributeError:
                raise AttributeError("evaluate static method is not yet assigned")
        else:
            Point.evaluate = evaluate

        self.input = []
        self.output = []
        self.input = np.asarray(copy.deepcopy(input))
        self.output = Point.evaluate(self.input)
        self.sub_space_index = Point.associate(self.output)

    @staticmethod
    def pareto_dominance(point1, point2):
        better = 0
        worse = 0
        equal = 0
        for i in range(point1.output.size):
            if point1.output[i] < point2.output[i]:
                better = better + 1
            elif point1.output[i] == point2.output[i]:
                equal = equal + 1
            elif point1.output[i] > point2.output[i]:
                worse = worse + 1

        if better == point1.output.size:
            return 2
        elif worse == point1.output.size:
            return -2
        elif better > 0 and worse == 0:
            return 1
        elif worse > 0 and better == 0:
            return -1
        else:
            return 0
