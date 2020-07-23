from arguments import parseArgs
from function import TestFunction
import numpy as np
from archive import Archive
from mutate import mutate
import random
from point import Point


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

            # check if current subspace is visited
            if cur_point.sub_space_index not in subspace_unvisited:
                # If current subspace is visited
                # select random point from an unvisited subspace
                cur_subspace_index = random.choice(subspace_unvisited)
                cur_point = random.choice(
                    ref_point_association_list[cur_subspace_index]
                )
                subspace_unvisited.remove(cur_subspace_index)

            new_point = mutate(cur_point)

            dominance = Point.pareto_dominance(new_point, cur_point)

            if dominance > 0:  # Case 1 cur_point dominates new_point
                pass
            elif dominance == 0:  # Case 2 new_point and cur_point non-dominating
                pass
            elif dominance < 0:  # Case 3 new_point dominates cur_point
                pass

            archive.resize()

        temp = temp * args.alpha

    # Show graph
    archive.show_output_graph()
