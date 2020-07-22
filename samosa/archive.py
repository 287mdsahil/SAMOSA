import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from point import Point
from function import TestFunction


class Archive:
    def __init__(self, hard_limit, soft_limit, test_function):
        self.hard_limit = hard_limit
        self.soft_limit = soft_limit
        self.test_function = test_function
        self.__initlize_points()

    def __initlize_points(self):
        self.points = np.asarray([], dtype=Point)

        for i in range(self.soft_limit):
            input = self.test_function.min_var + (
                self.test_function.max_var - self.test_function.min_var
            ) * np.random.uniform(size=self.test_function.n_var)
            point = Point(input, self.test_function.eval)
            self.add(point)

    def size(self):
        return self.points.size

    def add(self, point):
        self.points = np.append(self.points, [point])

    def show_output_graph(self):
        if self.test_function.n_objectives == 2:
            self.__show_2d_graph()
        elif self.test_function.n_objectives == 3:
            self.__show_3d_graph()
        else:
            # polar plot
            pass

    def __show_2d_graph(self):
        x = [p.output[0] for p in self.points]
        y = [p.output[1] for p in self.points]
        plt.plot(x, y, "ro")
        plt.show()

    def __show_3d_graph(self):
        x = [p.output[0] for p in self.points]
        y = [p.output[1] for p in self.points]
        z = [p.output[2] for p in self.points]
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.scatter3D(z, y, x)
        plt.show()
