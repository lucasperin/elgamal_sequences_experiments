import sys
from generate_tuple_data import run_experiment_cached, job_count_tuples_all, job_count_tuples


prime_filename = "../../primes/all_primes.csv"
prime_filename_v_is_g = "../../primes/gen_primes.csv"


def run_normal():
    print("Run Normal")
    return run_experiment_cached(prime_filename, job_count_tuples,False)


def run_v_is_g():
    print("Run v is g")
    return run_experiment_cached(prime_filename_v_is_g, job_count_tuples, True)


def run_normal_all():
    print("Run All Normal")
    return run_experiment_cached(prime_filename, job_count_tuples_all, False)


def run_v_is_g_all():
    print("Run All Normal")
    return run_experiment_cached(prime_filename_v_is_g, job_count_tuples_all, True)


functions = {
    'normal': run_normal,
    'v_is_g': run_v_is_g,
    'normal_all': run_normal_all,
    'v_is_g_all': run_v_is_g_all,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    sys.exit(func())
