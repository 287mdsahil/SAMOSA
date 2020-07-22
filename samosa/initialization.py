from function import TestFunction
import numpy as np


def init(args):
    print(args)
    # test
    t = TestFunction(args.problem_function, args.n_objectives)
    print(t.n_var)
    print(t.n_objectives)
    print(t.eval(np.random.rand(t.n_var)))
