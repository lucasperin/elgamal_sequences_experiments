import sys
from gen_run_data import run_experiment_cached


prime_filename = "../../primes/all_primes.csv"
prime_filename_v_is_g = "../../primes/gen_primes.csv"


def run_normal():
    print("Run Normal")
    return run_experiment_cached(prime_filename, False, False)


def run_thm_10():
    print("Run THM10")
    return run_experiment_cached(prime_filename, False, True)


def run_v_is_g():
    print("Run v is g")
    return run_experiment_cached(prime_filename_v_is_g, True, False)


functions = {
    'normal': run_normal,
    'thm10': run_thm_10,
    'v_is_g': run_v_is_g,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    sys.exit(func())
