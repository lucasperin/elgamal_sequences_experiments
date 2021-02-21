from tuples import *
from math_utils import *
import matplotlib.pyplot as plt
from multiprocessing import Pool
from functools import partial


def plot(t, g, p, v, bins):
    """
    :param t: tuple length
    :param g: plot for all generators up until g
    :param p: prime
    :param v: modulo
    :param bin: num of bins
    """
    plt.figure("t")
    count = binned_count(t, g, p, v, bins)
    keys = list(count.keys())
    w = list(count.keys())[0]*0.9
    plt.bar(keys, list(count.values()), width=w, tick_label=keys)
    plt.show()

