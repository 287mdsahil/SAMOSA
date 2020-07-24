from arguments import parseArgs
from function import TestFunction
import numpy as np
from archive import Archive
from mutate import mutate
import random
from amosa import amosa_select


def main():
    print("Running SAMOSA...")
    args = parseArgs()

    # Initialize test function
    test_function = TestFunction(args.problem_function, args.n_objectives)

    # Initialize archive
    archive = Archive(args.hard_limit, args.soft_limit, test_function)

    # Setting n_iter to multiple of ref_points.size closet to 500
    n_iter = archive.ref_points.size * round(500 / archive.ref_points.size)

    # Setting the cur_point
    cur_point = archive.get_random_point()

    # Setting array to denote which subspaces are unvisited
    subspace_unvisited = list(range(archive.ref_points.size))

    temp = args.max_temp
    while temp > args.min_temp:
        for i in range(n_iter):
            ref_point_association_list = archive.get_ref_point_association_list()

            # mark empty subspaces as visited
            for i in range(len(ref_point_association_list)):
                if len(ref_point_association_list[i]) == 0:
                    try:
                        subspace_unvisited.remove(i)
                    except ValueError:
                        pass

            if len(subspace_unvisited) == 0:
                subspace_unvisited = list(range(archive.ref_points.size))

            # check if current subspace is visited
            if cur_point.sub_space_index not in subspace_unvisited:
                # If current subspace is visited
                # select random point from an unvisited subspace
                cur_subspace_index = random.choice(subspace_unvisited)
                cur_point = random.choice(
                    ref_point_association_list[cur_subspace_index]
                )

            subspace_unvisited.remove(cur_point.sub_space_index)

            new_point = mutate(cur_point)
            cur_point = amosa_select(archive, cur_point, new_point, temp)
            archive.resize()
        temp = temp * args.alpha
        print(temp, archive.points.size)

    # Show graph
    archive.show_output_graph()
