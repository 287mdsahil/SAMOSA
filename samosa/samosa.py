from arguments import parseArgs
from function import TestFunction
import numpy as np
from archive import Archive
from mutate import mutate


def main():
    print("Running SAMOSA...")
    args = parseArgs()

    # Initialize test function
    test_function = TestFunction(args.problem_function, args.n_objectives)

    # Initialize archive
    archive = Archive(args.hard_limit, args.soft_limit, test_function)

    # Setting n_iter to multiple of ref_points.size closet to 500
    n_iter = archive.ref_points.size * round(500 / archive.ref_points.size)

    temp = args.max_temp
    while temp > args.min_temp:
        ref_point_association_list = archive.get_ref_point_association_list()

        temp = temp * args.alpha


    # Show graph
    archive.show_output_graph()
