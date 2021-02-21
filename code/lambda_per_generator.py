from tuples import *
from math_utils import *
import matplotlib.pyplot as plt
from multiprocessing import Pool
from functools import partial


def __job__(g, params):
    t, p, v = params
    c, _min, _max = tuple_count(t, g, p, v)
    return [(g, e) for e in c.values()]


def plot(t, g, p, v, threads = 10):
    """
    :param t: tuple length
    :param g: plot for all generators up until g
    :param p: prime
    :param v: modulo
    :param threads: num of threads
    """
    plt.figure("t")
    all_gens = sorted(n_generators(p, p))
    gens = [gen for gen in all_gens if gen <= g]
    lb, ub = bound_list(t, gens, p, v)
    leb, ueb = envelope_bound_list(t, gens, p, v)
    pool = Pool(threads)
    out = pool.map(partial(__job__, params=(t, p, v)), gens)
    for o in out:
        plt.scatter(*zip(*o))
    print(out)
    plt.plot(gens, lb, '--bv')
    plt.plot(gens, ub, '--rv')
    plt.plot(gens, ueb, '--yv')
    plt.plot(gens, leb, '--gv')
    plt.show()

