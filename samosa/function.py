from math import *
import sys
import numpy as np
import copy
import random
import time
import operator
import csv
from numpy import linalg as LA
from optproblems import wfg


class TestFunction:
    def __init__(self, problem_function, n_objectives):

        if problem_function == "SCH1":
            self.eval = self.SCH1
        elif problem_function == "SCH2":
            self.eval = self.SCH2
        elif problem_function == "DTLZ1":
            self.eval = self.DTLZ1
        elif problem_function == "DTLZ2":
            self.eval = self.DTLZ2
        elif problem_function == "DTLZ3":
            self.eval = self.DTLZ3
        elif problem_function == "DTLZ4":
            self.eval = self.DTLZ4
        elif problem_function == "ZDT1":
            self.eval = self.ZDT1
        elif problem_function == "ZDT2":
            self.eval = self.ZDT2
        elif problem_function == "ZDT3":
            self.eval = self.ZDT3
        elif problem_function == "ZDT4":
            self.eval = self.ZDT4
        elif problem_function == "ZDT6":
            self.eval = self.ZDT6
        elif problem_function == "IMB1":
            self.eval = self.IMB1
        elif problem_function == "IMB2":
            self.eval = self.IMB2
        elif problem_function == "IMB3":
            self.eval = self.IMB3
        elif problem_function == "IMB4":
            self.eval = self.IMB4
        elif problem_function == "IMB5":
            self.eval = self.IMB5
        elif problem_function == "IMB6":
            self.eval = self.IMB6
        elif problem_function == "IMB7":
            self.eval = self.IMB7
        elif problem_function == "IMB8":
            self.eval = self.IMB8
        elif problem_function == "IMB9":
            self.eval = self.IMB9
        elif problem_function == "IMB10":
            self.eval = self.IMB10
        else:
            raise ValueError("Invalid problem_function name")

        self.n_objectives = n_objectives
        self.n_var = 0
        if problem_function in ["SCH1", "SCH2"]:
            print("Number of objective functions: 2")
            print("Number of variables: 1")
            self.n_objectives = 2
            self.n_var = 1
        elif problem_function in ["DTLZ1", "DTLZ2", "DTLZ3", "DTLZ4"]:
            k = int()
            if problem_function == "DTLZ1":
                k = 5
            elif problem_function in ["DTLZ2", "DTLZ3", "DTLZ4"]:
                k = 10
            self.n_var = self.n_objectives + k - 1
            print("Number of variables: " + str(self.n_var))
        elif problem_function in ["ZDT1", "ZDT2", "ZDT3", "ZDT4", "ZDT5", "ZDT6"]:
            print("Number of objective functions: 2")
            self.n_objectives = 2
            self.n_var = int(input("Enter  the number of variables: "))
        elif problem_function in ["IMB1", "IMB2", "IMB3", "IMB7", "IMB8", "IMB9"]:
            print("Number of objective functions: 2")
            print("Number of variables: 10")
            self.n_objectives = 2
            self.n_var = 10
        elif problem_function in ["IMB4", "IMB5", "IMB6", "IMB10"]:
            print("Number of objective functions: 3")
            print("Number of variables: 10")
            self.n_objectives = 3
            self.n_var = 10

    def ZDT1(self, input_arr):
        f1 = input_arr[0]
        s = 0.0
        for i in range(1, len(input_arr)):
            s = s + input_arr[i]
        g = 1.0 + ((9.0 * s) / (len(input_arr) - 1.0))
        f2 = g * (1.0 - sqrt(f1 / g))
        return [f1, f2]

    def ZDT2(self, input_arr):
        f1 = input_arr[0]
        s = 0.0
        for i in range(1, len(input_arr)):
            s = s + input_arr[i]
        g = 1.0 + ((9.0 * s) / (len(input_arr) - 1.0))
        f2 = g * (1.0 - ((f1 / g) ** 2))
        return [f1, f2]

    def ZDT3(self, input_arr):
        f1 = input_arr[0]
        s = 0.0
        for i in range(1, len(input_arr)):
            s = s + input_arr[i]
        g = 1.0 + ((9.0 * s) / (len(input_arr) - 1.0))
        f2 = g * (1.0 - sqrt(f1 / g) - ((f1 / g) * sin(10.0 * 3.14 * f1)))
        return [f1, f2]

    def ZDT4(self, input_arr):
        f1 = input_arr[0]
        s = 0.0
        for i in range(1, len(input_arr)):
            s = s + ((input_arr[i] ** 2) - (10.0 * cos(4 * 3.14 * input_arr[i])))
        g = 1.0 + (10.0 * (len(input_arr) - 1.0)) + s
        f2 = g * (1.0 - ((f1 / g) ** 2))
        return [f1, f2]

    def ZDT6(self, input_arr):
        f1 = 1.0 - (exp(-4.0 * input_arr[0]) * ((sin(6.0 * 3.14 * input_arr[0])) ** 6))
        s = 0.0
        for i in range(1, len(input_arr)):
            s = s + input_arr[i]
        g = 1.0 + 9.0 * ((s / (len(input_arr) - 1.0)) ** 0.25)
        f2 = 1.0 - ((f1 / g) ** 2)
        return [f1, f2]

    def DTLZ1(self, input_arr):
        n_var = len(input_arr)
        k = n_var - self.n_objectives + 1
        out = [0.0] * self.n_objectives
        g = 0.0
        for i in range(n_var - k, n_var):
            g = g + ((input_arr[i] - 0.5) ** 2) - cos(20 * pi * (input_arr[i] - 0.5))
        g = 100 * (k + g)
        for i in range(1, self.n_objectives + 1):
            s = 0.5 * (1 + g)
            j = self.n_objectives - i
            while j >= 1:
                j = j - 1
                s = s * input_arr[j]
            if i > 1:
                s = s * (1 - input_arr[self.n_objectives - i])
            out[i - 1] = s
        return out

    def DTLZ2(self, input_arr):
        n_var = len(input_arr)
        k = n_var - self.n_objectives + 1
        out = [0.0] * self.n_objectives
        g = 0.0
        for i in range(n_var - k, n_var):
            g = g + ((input_arr[i] - 0.5) ** 2)
        for i in range(1, self.n_objectives + 1):
            s = 1.0 + g
            j = self.n_objectives - i
            while j >= 1:
                j = j - 1
                s = s * cos(pi * input_arr[j] * 0.5)
            if i > 1:
                s = s * sin(input_arr[self.n_objectives - i] * pi / 2)
            out[i - 1] = s
        return out

    def DTLZ3(self, input_arr):
        n_var = len(input_arr)
        k = n_var - self.n_objectives + 1
        g = 0.0
        for i in range(self.n_objectives - 1, n_var):
            g += ((input_arr[i] - 0.5) ** 2) - cos(20.0 * pi * (input_arr[i] - 0.5))
        g = (k + g) * 100
        out = [0.0] * self.n_objectives
        for m in range(0, self.n_objectives):
            product = 1 + g
            i = 0
            while (i + m) <= self.n_objectives - 2:
                product *= cos(input_arr[i] * pi / 2)
                i += 1
            if m > 0:
                product *= sin(input_arr[i] * pi / 2)
            out[m] = product
        return out

    def DTLZ4(self, input_arr, a=100):
        n_var = len(input_arr)
        k = n_var - self.n_objectives + 1
        g = 0.0
        for i in range(self.n_objectives - 1, n_var):
            g += (input_arr[i] - 0.5) ** 2
        out = [0.0] * self.n_objectives
        for m in range(0, self.n_objectives):
            product = 1 + g
            i = 0
            while (i + m) <= self.n_objectives - 2:
                product *= cos((input_arr[i] ** a) * pi / 2)
                i += 1
            if m > 0:
                product *= sin((input_arr[i] ** a) * pi / 2)
            out[m] = product
        return out

    def SCH1(self, input):
        func1 = input ** 2
        func2 = (input - 2.0) ** 2
        out = [func1, func2]
        return out

    def SCH2(self, input):
        func1 = float()
        if input <= 1:
            func1 = -input
        elif input > 1 and input <= 3:
            func1 = input - 2
        elif input > 3 and input <= 4:
            func1 = 4 - input
        else:
            func1 = input - 4
        func2 = (input - 5) ** 2
        out = [func1, func2]
        return out

    def IMB1(self, input_arr):
        n_var = len(input_arr)
        h = 0
        for i in range(1, n_var):
            t = abs(input_arr[i] - sin(0.5 * pi * input_arr[0]))
            h += 0.5 * ((-0.9 * t * t) + (t ** 0.6))
        g = 0
        if input_arr[0] > 0.2:
            g = h
        f1 = (1.0 + g) * input_arr[0]
        f2 = (1.0 + g) * (1 - sqrt(input_arr[0]))
        return [f1, f2]

    def IMB2(self, input_arr):
        n_var = len(input_arr)
        h = 0
        for i in range(1, n_var):
            t = abs(input_arr[i] - sin(0.5 * pi * input_arr[0]))
            h += 0.5 * ((-0.9 * t * t) + (t ** 0.6))
        g = 0
        if (input_arr[0] > 0.6) or (input_arr[0] < 0.4):
            g = h
        f1 = (1.0 + g) * input_arr[0]
        f2 = (1.0 + g) * (1 - input_arr[0])
        return [f1, f2]

    def IMB3(self, input_arr):
        n_var = len(input_arr)
        h = 0
        for i in range(1, n_var):
            t = abs(input_arr[i] - sin(0.5 * pi * input_arr[0]))
            h += 0.5 * ((-0.9 * t * t) + (t ** 0.6))
        g = 0
        if (input_arr[0] > 1.0) or (input_arr[0] < 0.8):
            g = h
        f1 = (1.0 + g) * cos(pi * input_arr[0] * 0.5)
        f2 = (1.0 + g) * sin(pi * input_arr[0] * 0.5)
        return [f1, f2]

    def IMB4(self, input_arr):
        n_var = len(input_arr)
        h = 0
        for i in range(2, n_var):
            t = abs(input_arr[i] - (0.5 * (input_arr[0] + input_arr[1])))
            h += 2.0 * cos(pi * 0.5 * input_arr[0]) * ((-0.9 * t * t) + (t ** 0.6))
        g = 0
        if (input_arr[0] > 1.0) or (input_arr[0] < 2.0 / 3.0):
            g = h
        f1 = (1.0 + g) * input_arr[0] * input_arr[1]
        f2 = (1.0 + g) * input_arr[0] * (1.0 - input_arr[1])
        f3 = (1.0 + g) * (1.0 - input_arr[0])
        return [f1, f2, f3]

    def IMB5(self, input_arr):
        n_var = len(input_arr)
        h = 0
        for i in range(2, n_var):
            t = abs(input_arr[i] - (0.5 * (input_arr[0] + input_arr[1])))
            h += 2.0 * cos(pi * 0.5 * input_arr[0]) * ((-0.9 * t * t) + (t ** 0.6))
        g = 0
        if (input_arr[0] > 0.5) or (input_arr[0] < 0.0):
            g = h
        f1 = (1.0 + g) * cos(pi * 0.5 * input_arr[0]) * cos(pi * 0.5 * input_arr[1])
        f2 = (1.0 + g) * cos(pi * 0.5 * input_arr[0]) * sin(pi * 0.5 * input_arr[1])
        f3 = (1.0 + g) * sin(pi * 0.5 * input_arr[0])
        return [f1, f2, f3]

    def IMB6(self, input_arr):
        n_var = len(input_arr)
        h = 0
        for i in range(2, n_var):
            t = abs(input_arr[i] - (0.5 * (input_arr[0] + input_arr[1])))
            h += 2.0 * cos(pi * 0.5 * input_arr[0]) * ((-0.9 * t * t) + (t ** 0.6))
        g = 0
        if (input_arr[0] > 0.75) or (input_arr[0] < 0.0):
            g = h
        f1 = (1.0 + g) * input_arr[0] * input_arr[1]
        f2 = (1.0 + g) * input_arr[0] * (1.0 - input_arr[1])
        f3 = (1.0 + g) * (1.0 - input_arr[0])
        return [f1, f2, f3]

    def IMB7(self, input_arr):
        n_var = len(input_arr)
        h1 = 0
        h2 = 0
        for i in range(1, n_var):
            s = abs(input_arr[i] - sin(0.5 * pi * input_arr[0]))
            t = abs(input_arr[i] - 0.5)
            h1 += 1.0 * ((-0.9 * s * s) + (s ** 0.6))
            h2 += t ** 0.6
        g = h1
        if (input_arr[0] > 0.8) or (input_arr[0] < 0.5):
            g = h2
        f1 = (1.0 + g) * input_arr[0]
        f2 = (1.0 + g) * (1 - sqrt(input_arr[0]))
        return [f1, f2]

    def IMB8(self, input_arr):
        n_var = len(input_arr)
        h1 = 0
        h2 = 0
        for i in range(1, n_var):
            s = abs(input_arr[i] - sin(0.5 * pi * input_arr[0]))
            t = abs(input_arr[i] - 0.5)
            h1 += 1.0 * ((-0.9 * s * s) + (s ** 0.6))
            h2 += t ** 0.6
        g = h1
        if (input_arr[0] > 0.8) or (input_arr[0] < 0.5):
            g = h2
        f1 = (1.0 + g) * input_arr[0]
        f2 = (1.0 + g) * (1 - input_arr[0])
        return [f1, f2]

    def IMB9(self, input_arr):
        n_var = len(input_arr)
        h1 = 0
        h2 = 0
        for i in range(1, n_var):
            s = abs(input_arr[i] - sin(0.5 * pi * input_arr[0]))
            t = abs(input_arr[i] - 0.5)
            h1 += 1.0 * ((-0.9 * s * s) + (s ** 0.6))
            h2 += t ** 0.6
        g = h1
        if (input_arr[0] > 0.8) or (input_arr[0] < 0.5):
            g = h2
        f1 = (1.0 + g) * cos(pi * 0.5 * input_arr[0])
        f2 = (1.0 + g) * sin(pi * 0.5 * input_arr[0])
        return [f1, f2]

    def IMB10(self, input_arr):
        n_var = len(input_arr)
        h1 = 0
        h2 = 0
        for i in range(2, n_var):
            s = abs(input_arr[i] - (0.5 * (input_arr[0] + input_arr[1])))
            t = abs(input_arr[i] - (input_arr[0] * input_arr[1]))
            h1 += 2.0 * ((-0.9 * s * s) + (s ** 0.6))
            h2 += t ** 0.6
        g = h1
        if ((input_arr[0] > 0.8) or (input_arr[0] < 0.2)) or (
            (input_arr[1] > 0.8) or (input_arr[1] < 0.2)
        ):
            g = h2
        f1 = (1.0 + g) * input_arr[0] * input_arr[1]
        f2 = (1.0 + g) * input_arr[0] * (1.0 - input_arr[1])
        f3 = (1.0 + g) * (1.0 - input_arr[0])
        return [f1, f2, f3]
