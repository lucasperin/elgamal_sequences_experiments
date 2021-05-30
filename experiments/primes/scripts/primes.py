from multiprocessing import Pool, Array
from common.primes import *
from common.math_utils import *

# T_RANGE = 7 #start at 2
v_range = 7
FILE_NAME = "../all_primes.csv"
NUM_OF_GENS = 10
USE_V_IS_G: bool = False

def __find_primes__(prime):
    p = int(prime)
    gens = []
    global v_array
    global USE_V_IS_G
    if USE_V_IS_G:
        gens = sorted(n_generators(p,p))[:v_range+1]
    params = []
    for v in range(2, 2 + v_range):
        if (p - 1) % v == 0:
            if v_array[v - 2] > 0:
                if not USE_V_IS_G:
                    params.append((p, v))
                    v_array[v - 2] -= 1
                elif v in gens:
                    params.append((p, v))
                    v_array[v - 2] -= 1
        print(list(v_array))
    return params

def run_experiment(use_v_is_g=False):
    N = 100
    global v_array
    v_array = Array('i', [N] * v_range)
    global USE_V_IS_G
    if use_v_is_g:
        v_array[2] = 0
        v_array[3] = 0
        v_array[6] = 0
        USE_V_IS_G = True

    THREADS = 10
    p_list = primes_starting_at(1100000, 1500000)[:3000]
    l = len(p_list)
    idx=0
    pool = Pool(THREADS) #, initializer=init_varray, initargs=v_array)
    primes = []
    while(sum(v_array) > 0) and ((idx+THREADS) <= l):
        params = pool.map(__find_primes__, p_list[idx:idx+THREADS])
        idx += THREADS
        for e in params:
            primes += e

    filename = FILE_NAME.format("all")
    if use_v_is_g:
        filename = FILE_NAME.format("gen")

    with open(filename, 'w') as f:
        for val in primes:
            p, v = val
            f.write("{}\t{}\n".format(p, v))

if __name__ == "__main__":
    run_experiment(False)