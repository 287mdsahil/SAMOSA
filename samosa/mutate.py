from point import Point
from math import *
import numpy as np
import random
import copy


def laplacian(input, max_input, min_input, b=0.25):
    """Function to perform mutation on individual input vector"""

    i_rand = random.randint(0, input.size - 1)
    y = input[i_rand]
    y = laplacian_mutate(y, b)
    i_count = 0
    while (y < min_input[i_rand] or y > max_input[i_rand]) and i_count < 20:
        y = input[i_rand]
        y = laplacian_mutate(y, b)
        i_count = i_count + 1

    if y < min_input[i_rand]:
        y = min_input[i_rand]
    elif y > max_input[i_rand]:
        y = max_input[i_rand]

    # Update input vector element
    input[i_rand] = y
    return input


def laplacian_mutate(y, b):
    """Perform mutation on individual vector element"""
    d_rand = 0
    while d_rand == 0:
        d_rand = random.uniform(-0.5, 0.5)
    d_rand_lap = int()
    if d_rand < 0:
        d_rand_lap = b * log(1 - 2 * fabs(d_rand))
    else:
        d_rand_lap = -b * log(1 - 2 * fabs(d_rand))
    y = y + d_rand_lap
    return y


def mutate(point, max_input=None, min_input=None):
    if max_input == None:
        max_input = np.ones(point.input.size)
    if min_input == None:
        min_input = np.zeros(point.input.size)
    input = copy.deepcopy(point.input)
    laplacian(input, max_input, min_input)
    new_point = Point(input, point.evaluate)
    return new_point
