from tuples import *
from math_utils import *
import matplotlib.pyplot as plt
from multiprocessing import Pool
from functools import partial
from mpl_toolkits import mplot3d


def __job__(t, params):
    g_range, p, v = params
    all_gens = sorted(n_generators(p, p))
    gens = [gen for gen in all_gens if gen <= g_range]
    ret = []
    for g in gens:
        c, _min, _max = tuple_count(t, g, p, v)
        l, u, _ = tuple_bound(t, g, p, v)
        if _min - l > u - _max :
            ret.append((t, g, _min - l, 'blue'))
        else:
            ret.append((t, g, u - _max, 'red'))
    return ret


def plot(t_range, g_range, p, v):
    ax = plt.axes(projection='3d')
    x = []
    y = []
    z = []
    pool = Pool(t_range-1)
    out = pool.map(partial(__job__, params=(g_range, p, v)), range(2,t_range+1))
    for i in out:
        for j in i:
            ax.scatter(j[0], j[1], j[2], cmap='viridis', color=j[3])
    plt.xlabel('t')
    plt.ylabel('generators')
    ax.set_zlabel('Max Delta')
    plt.show()
