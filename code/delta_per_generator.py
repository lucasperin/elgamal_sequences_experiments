from tuples import *
from math_utils import *
import matplotlib.pyplot as plt
from multiprocessing import Pool
from functools import partial


def __job__(g, params):
    t, p, v = params
    print(g)
    print("Computing t={} g={} p={} v={}".format(t,g,p,v), end='\r')
    c, _min, _max = tuple_count(t, g, p, v)
    return (g, _min), (g,_max)

def __job2__(g, params):
    t, p, v = params
    #print(g)
    print("Computing t={} g={} p={} v={}".format(t,g,p,v))
    c, _min, _max = tuple_count(t, g, p, v)
    return (g, c)

def plot(t, gens, p, v, threads = 10, show=False):
    """
    :param t: tuple length
    :param g: plot for all generators up until g
    :param p: prime
    :param v: modulo
    :param threads: num of threads
    """
    plt.clf()
    pool = Pool(threads)
    out = pool.map(partial(__job__, params=(t, p, v)), gens)
    ub, lb = [], []
    for o in out:
        cur_g = o[0][0]
        l, u, _ = tuple_bound(t,cur_g,p,v)
        lb_plot = o[0][1]- l
        ub_plot = u - o[1][1]
        lb.append((cur_g, lb_plot))
        ub.append((cur_g, ub_plot))
    print()
    plt.plot(*zip(*lb), '--bx', label='Lower bound')
    plt.plot(*zip(*ub), '--ro', label='Upper bound')
    plt.xlabel('Generators')
    plt.ylabel('Bound delta')
    plt.legend(loc='upper left')
    name = "Bound delta all values p={} v={} and t={}".format(p,v,t)
    plt.title(name)
    plt.ylim(0, 21)
    if show:
        plt.show()
    else:
        plt.savefig("E:\{}".format(name), bbox_inches='tight')

def plot_all_counts(t, gens, p, v, threads = 10, show=False):
    """
    :param t: tuple length
    :param g: plot for all generators up until g
    :param p: prime
    :param v: modulo
    :param threads: num of threads
    """
    plt.clf()
    pool = Pool(threads)
    out = pool.map(partial(__job2__, params=(t, p, v)), gens)
    ub, lb = [], []
    for o in out:
        cur_g = o[0]
        l, u, _ = tuple_bound(t,cur_g,p,v)
        for val in o[1].values():
            lb.append((cur_g, min(20, val - l)))
            ub.append((cur_g, min(20, u - val)))
            #plt.scatter((cur_g), (val - l), marker='x', color='blue', label='Lower Bound Delta')
            #plt.scatter(cur_g, u - val, marker='o', color='red', label='Upper Bound Delta')
    print()
    plt.scatter(*zip(*lb), marker='x', color='blue', label='Lower bound')
    plt.scatter(*zip(*ub), marker='o', color='red', label='Upper bound')
    plt.xlabel('Generators')
    plt.ylabel('Bound delta')
    plt.legend(loc='upper left')
    name = "Bound delta p={} v={} and t={}".format(p,v,t)
    plt.title(name)
    plt.ylim(0, 21)
    if show:
        plt.show()
    else:
        plt.savefig("E:\{}".format(name), bbox_inches='tight')


def plot_ratio(t, gens, p, v, threads=10, show=False):
    """
    :param t: tuple length
    :param g: plot for all generators up until g
    :param p: prime
    :param v: modulo
    :param threads: num of threads
    """
    plt.clf()
    pool = Pool(threads)
    out = pool.map(partial(__job__, params=(t, p, v)), gens)
    ub, lb = [], []
    for o in out:
        cur_g = o[0][0]
        l, u, _ = tuple_bound(t,cur_g,p,v)
        if o[0][1] == 0:
            lr = 0
        else:
            lr = 1 - l/o[0][1]
        ur = u/o[1][1] - 1
        lb.append((cur_g, lr))
        ub.append((cur_g, ur))
    plt.plot(*zip(*lb), '--bo', label='Lower bound')
    plt.plot(*zip(*ub), '--ro', label='Upper bound')
    plt.xlabel('Generators')
    plt.ylabel('Bound delta ratio')
    plt.legend(loc='upper left')
    name = "Bound delta ratio p={} v={} and t={}".format(p,v,t)
    plt.title(name)
    if show:
        plt.show()
    else:
        plt.savefig("E:\{}".format(name), bbox_inches='tight')

def plot_hybrid(t, gens, p, v, threads = 10, show=False):
    """
    :param t: tuple length
    :param g: plot for all generators up until g
    :param p: prime
    :param v: modulo
    :param threads: num of threads
    """
    plt.clf()
    pool = Pool(threads)
    out = pool.map(partial(__job__, params=(t, p, v)), gens)
    ub, lb = [], []
    for o in out:
        cur_g = o[0][0]
        l, u, _ = tuple_bound(t, cur_g, p, v)
        el, eu = tuple_envelope_bound(t, cur_g, p, v)
        l = max(l, el)
        u = min(u, eu)
        lb_plot = abs(o[0][1]- l)
        ub_plot = abs(o[1][1]- l)
        lb.append((cur_g, lb_plot))
        ub.append((cur_g, ub_plot))
    #plt.plot(*zip(*lb), '--go', label='Lower bound')
    #plt.plot(*zip(*ub), '--yo', label='Upper bound')
    plt.scatter(*zip(*lb), label='Lower bound')
    plt.scatter(*zip(*ub), label='Upper bound')
    plt.xlabel('Generators')
    plt.ylabel('Bound delta')
    plt.legend(loc='upper left')
    name = "Hybrid Bound delta p={} v={} and t={}".format(p,v,t)
    plt.title(name)
    if show:
        plt.show()
    else:
        plt.savefig("E:\{}".format(name), bbox_inches='tight')

