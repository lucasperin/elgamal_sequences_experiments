import sys
sys.path.append("../../../")

import csv
from multiprocessing import Pool
from tqdm import tqdm
from common.math_utils import *
from common.tuples import tuple_count_range


T_RANGE = 7 #start at 2
F_NAME = "../output/tuples_{}_{}.csv"
NUM_OF_GENS = 10
CSV_DELIMITER='\t'
USE_V_IS_G = False


def __job_count_bounds__(params):
    global USE_V_IS_G
    p, v, isgen = params

    if USE_V_IS_G:
        gens = [v]
    else:
        gens = sorted(n_generators(p, p))[:NUM_OF_GENS]

    with open(F_NAME.format(p, v), 'w') as f:
        for g in gens:
            if g >= v:
                f.write("{}\t{}\t{}".format(p, v, g))
                actual_count = tuple_count_range(T_RANGE, g, p, v)
                for t in range(1, T_RANGE + 1):
                    vals = [val for key, val, in actual_count.items() if len(key) == t]
                    if len(vals) > 0:
                        f.write("\t{}\t{}\t{}".format(min(vals), max(vals), sum(vals)))
                f.write("\n")


def run_experiment_cached(prime_filename, use_v_is_g=False):
    global USE_V_IS_G
    if use_v_is_g:
        USE_V_IS_G = True

    params = []
    with open(prime_filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        for row in reader:
            params.append((int(row[0]), int(row[1]), row[2]))

    THREADS = 10
    pool = Pool(THREADS)
    for _ in tqdm(pool.imap_unordered(__job_count_bounds__, params), total=len(params)):
        pass


if __name__ == '__main__':
    prime_filename = "../../primes/all_primes.csv"
    prime_filename_v_is_v = "../../primes/gen_primes.csv"
    run_experiment_cached(prime_filename_v_is_v, True)
