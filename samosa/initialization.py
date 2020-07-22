from function import TestFunction
import numpy as np
from archive import Archive


def init(args):
    print(args)

    # Initialize test function
    test_function = TestFunction(args.problem_function, args.n_objectives)

    # Initialize archive
    archive = Archive(args.hard_limit, args.soft_limit, test_function)

    for p in archive.points:
        print(p.output)

    archive.show_output_graph()
