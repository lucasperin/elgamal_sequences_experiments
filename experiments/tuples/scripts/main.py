import sys
from generate_tuple_data import run_experiment_cached


prime_filename = "../../primes/all_primes.csv"
prime_filename_v_is_g = "../../primes/gen_primes.csv"


def run_normal():
    print("Run Normal")
    return run_experiment_cached(prime_filename, False)


def run_v_is_g():
    print("Run v is g")
    return run_experiment_cached(prime_filename_v_is_g, True)


functions = {
    'normal': run_normal,
    'v_is_g': run_v_is_g,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    sys.exit(func())
