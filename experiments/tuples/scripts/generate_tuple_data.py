import sys
sys.path.append("../../../")

import csv
from multiprocessing import Pool
from tqdm import tqdm
from common.math_utils import *
from common.tuples import tuple_count_range


T_MIN=2
T_MAX=7
T_NUM=(T_MAX-T_MIN)+1
F_NAME = "../output/tuples_{}_{}.csv"
NUM_OF_GENS = 10
CSV_DELIMITER='\t'
USE_V_IS_G = False

def job_count_tuples_all(params):
    global USE_V_IS_G
    p, v = params

    if USE_V_IS_G:
        gens = [v]
    else:
        gens = sorted(n_generators(p, p))[:NUM_OF_GENS]

    with open(F_NAME.format(p, v), 'w') as f:
        for g in gens:
            if g >= v:
                actual_count = tuple_count_range(T_MAX, g, p, v)
                for t in range(T_MIN, T_MAX + 1):
                    f.write("{}\t{}\t{}\t{}".format(p, v, g, t))
                    vals = [val for key, val, in actual_count.items() if len(key) == t]
                    for val in vals:
                        f.write("\t{}".format(val))
                    f.write("\n")
                # lines = [""]*T_NUM
                # for i in range(T_NUM):
                #     lines[i] = "{}\t{}\t{}\t{}".format(p, v, g, i+T_MIN)
                # for key, val, in actual_count.items():
                #     if len(key) > 1:
                #         lines[len(key) - T_MIN] += "\t{}\t{}".format(key, val)
                # for line in lines:
                #     f.write(line + "\n")


def job_count_tuples(params):
    global USE_V_IS_G
    p, v = params

    if USE_V_IS_G:
        gens = [v]
    else:
        gens = sorted(n_generators(p, p))[:NUM_OF_GENS]

    with open(F_NAME.format(p, v), 'w') as f:
        for g in gens:
            if g >= v:
                f.write("{}\t{}\t{}".format(p, v, g))
                actual_count = tuple_count_range(T_MAX, g, p, v)
                for t in range(T_MIN, T_MAX + 1):
                    vals = [val for key, val, in actual_count.items() if len(key) == t]
                    if len(vals) > 0:
                        f.write("\t{}\t{}\t{}".format(min(vals), max(vals), sum(vals)))
                f.write("\n")


def run_experiment_cached(prime_filename, job_name, use_v_is_g=False):
    global USE_V_IS_G
    if use_v_is_g:
        print("Using v as generator")
        USE_V_IS_G = True

    params = []
    with open(prime_filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        for row in reader:
            params.append((int(row[0]), int(row[1])))

    THREADS = 10
    pool = Pool(THREADS)
    for _ in tqdm(pool.imap_unordered(job_name, params), total=len(params)):
        pass


if __name__ == '__main__':
    job_count_tuples_all((1200023, 7))
