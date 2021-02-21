from tuples import *
from multiprocessing import Pool, Array
from functools import partial
from math_utils import *
from primes import primes_starting_at
from datetime import datetime

T_RANGE = 7 #start at 2
F_NAME = "~/Public/experiments/tuples/{}_{}_delta_zero.csv"

def __job_count_bounds__(params):
    p, v, isgen = params
    gens = sorted(n_generators(p, p))[:1000]
    count_upper = [0]*(T_RANGE-1)
    count_lower = [0]*(T_RANGE-1)
    for g in gens:
        if g >= v:
            print(g, p, v)
            count = tuple_count_range(T_RANGE, g, p, v)
            for t in range(2,T_RANGE+1):
                l, u, _ = tuple_bound(t, g, p, v)
                vals = [val for key, val, in count.items() if len(key) == t]
                if( (min(vals) -l) == 0 ):
                    count_lower[t-2]+=1
                if ((u - max(vals)) == 0):
                    count_upper[t-2]+=1

    with open(F_NAME.format(p, v), 'w') as f:

        #f.write("prime\tv\tisgen\tbound")
        #for t in range(2, T_RANGE+1):
        #    f.write("\tt{}".format(t))

        #f.write("\n{}\t{}\t{}\tlower".format(p, v, isgen))
        f.write("{}\t{}\t{}\tlower".format(p, v, isgen))
        for c in count_lower:
            f.write("\t{}".format(c))

        f.write("\n{}\t{}\t{}\tupper".format(p, v, isgen))
        for c in count_upper:
            f.write("\t{}".format(c))
        f.write("\n")


def __job_count_bounds_2__(params):
    print(params)
    p, v, isgen = params
    g = 0
    if isgen == "yes":
        gens = [v]
    else:
        gens = sorted(n_generators(p, p))[:10]
    
    with open(F_NAME.format(p, v), 'w') as f:
        for g in gens:
            if g >= v:
                f.write("{}\t{}\t{}".format(p, v, g))
                actual_count = tuple_count_range(T_RANGE, g, p, v)
                for t in range(2,T_RANGE+1):
                    vals = [val for key, val, in actual_count.items() if len(key) == t]
                    current_lower = min(vals)
                    current_upper = max(vals)
                    f.write("\t{}\t{}\t{}\t{}".format(current_lower, vals.count(current_lower), current_upper, vals.count(current_upper)))
                f.write("\n")


v_range = 8
def init_varray(v_is, v_no):
    global v_isgen, v_nogen
    v_isgen = v_is
    v_nogen = v_no

def __find_primes__(prime):
    p = int(prime)
    gens = sorted(n_generators(p,p))[:v_range]
    params = []
    for v in range(2, 2 + v_range):
        if (p - 1) % v == 0:
            if (v in gens) and (v_isgen[v - 2] > 0):
                params.append((p,v, "yes"))
                v_isgen[v - 2] -= 1;
            elif v_nogen[v - 2] > 0:
                params.append((p,v, "no"))
                v_nogen[v - 2] -= 1;
    return params

def run_experiment():
    with open(F_NAME.format('start', 0), 'w') as f:
        f.write("start at {}!".format(datetime.now().strftime('%d/%m/%Y %H:%M:%s')))
    N = 100
    v_is = Array('i', [N] * v_range)
    v_no = Array('i', [N] * v_range)
    THREADS = 20
    p_list = primes_starting_at(1100000,1500000)[:1000]
    l = len(p_list)
    idx=0
    pool = Pool(THREADS, initializer=init_varray, initargs=(v_is, v_no))
    params = []
    while(sum(v_is)+sum(v_no) > 0) and ((idx+THREADS) <= l):
        out = pool.map(__find_primes__, p_list[idx:idx+THREADS])
        idx+=THREADS
        for e in out:
            params += e

    THREADS = 10
    pool = Pool(THREADS)
    pool.map(__job_count_bounds_2__, params)
    with open(F_NAME.format('stop', 0), 'w') as f:
        f.write("Done at {}!".format(datetime.now().strftime('%d/%m/%Y %H:%M:%s')))


