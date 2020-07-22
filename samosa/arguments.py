import argparse


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "problem_function", help="Name of the problem function set to optimize"
    )
    parser.add_argument("n_objectives", help="Number of objective functions")
    parser.add_argument("hard_limit", help="Hard limit")
    parser.add_argument("soft_limit", help="Soft limit")
    parser.add_argument("alpha", help="Alpha value")

    parser.add_argument("--n-iter", help="Number of iterations per temperature")
    parser.add_argument("--max-temp", help="Maximum temperature")
    parser.add_argument("--min-temp" , help="Minimum temperature")

    args = parser.parse_args()

    args.n_objectives = int(args.n_objectives)
    args.hard_limit = int(args.hard_limit)
    args.soft_limit = int(args.soft_limit)
    args.alpha = float(args.alpha)
    if args.n_iter is not None:
        args.n_iter = int(args.n_iter)
    else:
        args.n_iter = 500

    if args.max_temp is not None:
        args.max_temp = float(args.max_temp)
    else:
        args.max_temp = 200.0

    if args.min_temp is not None:
        args.min_temp = float(args.min_temp)
    else:
        args.min_temp = 0.0000001

    return args
