from function import TestFunction
import numpy as np
from archive import Archive
from mutate import mutate


def init(args):
    print(args)

    # Initialize test function
    test_function = TestFunction(args.problem_function, args.n_objectives)

    # Initialize archive
    archive = Archive(args.hard_limit, args.soft_limit, test_function)

    #mutate
    print(archive.points[0].input)
    mutate(archive.points[0])
    print(archive.points[0].input)

