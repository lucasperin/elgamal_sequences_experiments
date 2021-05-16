import delta_per_generator
import delta_surface
import lambda_histogram
from common.tuples import *
import lambda_per_generator
from common.math_utils import *
import run_delta_zero
import os

os.nice(19)

def plot_hybrid_delta(t, g, p, v, show=True):
    delta_per_generator.plot_hybrid(t, g, p, v, show=show)

def plot_delta_without_explosion(t, p, v, show=True):
    g = floor(p**(1/(t-1)))
    print("Plotting t={} p={} v={} with g up to {}".format(t,p,v,g))
    delta_per_generator.plot(t, g, p, v, show=show)

def plot_surface():
    delta_surface.plot(10, 10, 1020137, 2)

def plot_bins(t, p, v):
    g = first_generator(p)
    lambda_histogram.plot(t, g, p, v, 5)

def plot_lambda_per_gen(t, gmax, p, v):
    lambda_per_generator.plot(t, gmax, p, v)

def gen_list(g, p):
    all_gens = sorted(n_generators(p, p))
    return [gen for gen in all_gens if gen <= g]

def print_gens():
    primes = [
    1000003,
    1000033,
    1000037,
    1000039,
    1000081,
    1000099,
    1000117,
    1000121,
    1000133,
    1000151,
    1000159,
    1000171,
    1000183,
    1000187,
    1000193,
    1000199,
    1000211,
    1000213,
    1000231,
    1000249,
    1000253,
    1000273,
    1000289,
    1000291,
    1000303,
    1000313,
    1000333,
    1000357,
    1000367,
    1000381,
    1000393,
    1000397,
    1000403,
    1000409,
    1000423,
    1000427,
    1000429,
    1000453,
    1000457,
    1000507,
    1000537,
    1000541,
    1000547,
    1000577,
    1000579,
    1000589]

    for p in primes:
        gens = sorted(n_generators(p, p))[:20]
        print(p, gens)


if __name__ == '__main__':
    """
    t - length of tuple
    g - generator
    p - prime
    v - modulo
    """
    t = 3
    #p = 1020137
    #p = 1020143
    p = 1020157
    #p = 1020163
    #p = 1020223
    #p = 1020233
    #p = 1020247
    v = 4
    #gens = sorted(n_generators(p, p))[:20]
    #plot_delta_without_explosion(t,p,v, show=True)
    #delta_per_generator.plot(t,g,p,v, show=True)
    #delta_per_generator.plot_ratio(t,g,p,v)
    #plot_surface()
    #plot_bins(t, p, v)
    #plot_lambda_per_gen(t, g, p, v)
    #plot_hybrid_delta(t, g, p, v)
    #delta_per_generator.plot_hybrid(t, g, p, v)
    #delta_per_generator.plot(t, gens, p, v, show=True)
    #delta_per_generator.plot_hybrid(t, gens[100:1000], p, v)
    #delta_per_generator.plot_all_counts(t, gens[:100], p, v, show=True)
    #delta_zero.run_experiment()
    run_delta_zero.run_experiment()
    #print_gens();
    print("Finished")



