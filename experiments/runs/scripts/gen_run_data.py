import sys
sys.path.append("../../../")

import csv
from multiprocessing import Pool
from tqdm import tqdm
from common.math_utils import *
from common.runs import run_count


T_RANGE = 7 #start at 2
F_NAME = "../output/runs_{}_{}.csv"
NUM_OF_GENS = 10
CSV_DELIMITER='\t'
USE_V_IS_G = False
THM_TEN = False


def __job_count_bounds__(params):
    global USE_V_IS_G
    # print(params)
    p, v, isgen = params

    gens = []
    if USE_V_IS_G:
        gens = [v]
    else:
        aux = sorted(n_generators(p, p))
        if THM_TEN:
            i = 0
            while len(gens) < NUM_OF_GENS:
                if gcd(aux[i], v) == 1:
                    gens.append(aux[i])
                i += 1
        else:
            gens = aux[:NUM_OF_GENS]


    with open(F_NAME.format(p, v), 'w') as f:
        for g in gens:
            if g >= v:
                f.write("{}\t{}\t{}".format(p, v, g))
                actual_count, t_range = run_count(g, p, v)
                for t in range(1, T_RANGE + 1):
                    vals = [val for key, val, in actual_count.items() if len(key) == t]
                    if len(vals) > 0:
                        f.write("\t{}\t{}\t{}".format(min(vals), max(vals), sum(vals)))
                f.write("\n")


def run_experiment_cached(prime_filename, use_v_is_g, theorem_ten):
    global USE_V_IS_G
    global THM_TEN
    if use_v_is_g:
        USE_V_IS_G = True
        print("Using v as generator")
    if theorem_ten:
        print("Theorem 10 enabled, using g and v co-prime")
        THM_TEN = True

    params = []
    with open(prime_filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        for row in reader:
            params.append((int(row[0]), int(row[1]), row[2]))

    THREADS = 10
    pool = Pool(THREADS)
    for _ in tqdm(pool.imap_unordered(__job_count_bounds__, params), total=len(params)):
        pass

    return 0


if __name__ == '__main__':
    prime_filename = "../../primes/all_primes.csv"
    prime_filename_v_is_g = "../../primes/gen_primes.csv"
    run_experiment_cached(prime_filename_v_is_g, True, True)
