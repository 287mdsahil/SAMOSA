import copy
import numpy as np
import math


class Point:
    def __init__(self, input, evaluate=None, ref_points=None):
        # Check if ref_points is assigned
        if ref_points is None:
            try:
                Point.ref_points
            except AttributeError:
                raise AttributeError("ref_points static variable is not yet assigned")
        else:
            Point.ref_points = ref_points
        # Check if evaluate function is defined
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
        self.sub_space_index = Point.associate(self.output, Point.ref_points)

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

    @staticmethod
    def associate(output, ref_points):
        min_d2 = math.inf
        ref_index = 0
        for i in range(len(ref_points)):
            d1, d2 = Point.calculateD1D2(output, ref_points[i])
            if d2 < min_d2:
                min_d2 = d2
                ref_index = i
        return ref_index

    @staticmethod
    def calculateD1D2(output, ref_point):
        # calculate d1
        refPointMod = 0.0
        for x in ref_point:
            refPointMod = refPointMod + x * x
        refPointMod = math.sqrt(refPointMod)

        d1 = 0.0
        for i in range(len(output)):
            d1 = d1 + output[i] * ref_point[i]
        d1 = d1 / refPointMod

        # calculate d2
        pointOnRef = copy.deepcopy(ref_point)
        for i in range(len(pointOnRef)):
            pointOnRef[i] = pointOnRef[i] * d1 / refPointMod

        d2Vector = []
        d2 = 0
        for i in range(len(output)):
            d2Vector.append(output[i] - pointOnRef[i])
            d2 = d2 + (output[i] - pointOnRef[i]) ** 2
        d2 = math.sqrt(d2)

        return d1, d2

    @staticmethod
    def calculatePBI(output, ref_point):
        theta = 5
        d1, d2 = Point.calculateD1D2(output, ref_point)
        return d1 + theta * d2
