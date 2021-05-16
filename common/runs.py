from collections import defaultdict
from common.math_utils import element_at, n_generators


def run_count(generator, prime, modulo):
    g, p, v = generator, prime, modulo
    count = defaultdict(lambda: 0)
    current_element = element_at(0, g, p, v)
    tail = 0
    for i in range(1, p-1):
        tail += 1
        if element_at(i, g, p, v) != current_element:
            break

    current_element = element_at(tail, g, p, v)
    run_len = 1
    for i in range(tail+1, p + tail):
        next_element = element_at(i, g, p, v)
        if next_element == current_element:
            run_len += 1
        else:
            index = [current_element]*run_len
            count[tuple(index)] += 1
            run_len = 1
            current_element = next_element
    length = len(max(count.keys()))
    for e in range(v):
        for t in range(1, length+1):
            count[tuple([e]*t)] += 0
    return count, length

def run_len_count(t_range, generator, prime, modulo):
    g, p, v = generator, prime, modulo
    count = defaultdict(lambda: 0)
    for t in range(1, t_range+1):
        count[t] = 0
    current_element = element_at(0, g, p, v)
    tail = 0
    for i in range(1, p-1):
        tail += 1
        if element_at(i, g, p, v) != current_element:
            break

    current_element = element_at(tail, g, p, v)
    run_len = 1
    for i in range(tail+1, p + tail):
        next_element = element_at(i, g, p, v)
        if next_element == current_element:
            run_len += 1
        else:
            count[run_len] += 1
            run_len = 1
            current_element = next_element
    return count

if __name__ == "__main__":
    p = 1100023
    v = 3
    g = 0
    gens = sorted(n_generators(p, p))[:10]
    print(gens)
    for g in gens:
        if g >= v:
            print("{}\t{}\t{}".format(p, v, g))
            actual_count, t_range = run_count(g, p, v)
            print(actual_count, t_range)
            for t in range(1,7+1):
                vals = [val for key, val, in actual_count.items() if len(key) == t]
                current_lower = min(vals)
                current_upper = max(vals)
                print("\t{}\t{}\t{}\t{}".format(current_lower, vals.count(current_lower), current_upper, vals.count(current_upper)))
                print("\n")


