from itertools import product
from math import ceil, floor
from common.math_utils import element_at



# pos(i) = x  pos(i +N/2) = 1 - x
# can we optimize by computing half of the sequence??
#@lru_cache(maxsize=2048)
def tuple_count(length, generator, prime, modulo):
    count = {key:0 for key in product(range(modulo), repeat=length)}
    current = []
    for i in range(length):
        current.append(element_at(i, generator, prime, modulo))

    for i in range(prime-1):
        count[tuple(current)] += 1
        current = current[1:]
        current.append(element_at(i+length, generator, prime, modulo))

    return count, min(count.values()), max(count.values())

def tuple_count_range(length, generator, prime, modulo):
    count = {}
    for t in range(1,length+1):
        count.update({key: 0 for key in product(range(modulo), repeat=t)})
    current = []
    for i in range(length):
        current.append(element_at(i, generator, prime, modulo))

    for i in range(prime-1):
        for j in range(1, length + 1):
            count[tuple(current[:j])] += 1
        current = current[1:]
        current.append(element_at(i+length, generator, prime, modulo))

    return count

def tuple_bound(length, generator, prime, modulo):
    t, g, p, v = length, generator, prime, modulo
    q = floor(p / (pow(g, t - 1)))
    lower = pow(floor(g / v), t - 1) * floor(q / v)
    upper = pow(ceil(g / v), t - 1) * (floor(q / v) + 1)
    return lower, upper, q


def tuple_envelope_bound(length, generator, prime, modulo):
    t, g, p, v = length, generator, prime, modulo
    ueb = (p/v) * ((g+v)/(g*v))**(t-1)
    leb = (p/v) * ((g-v)/(g*v))**(t-1)
    return leb, ueb


def bound_list(t, gens, p, v):
    lb, ub = [], []
    for g in gens:
        l, u, _ = tuple_bound(t, g, p, v)
        lb.append(l)
        ub.append(u)
    return lb, ub


def envelope_bound_list(t, gens, p, v):
    lb, ub = [], []
    for g in gens:
        l, u = tuple_envelope_bound(t, g, p, v)
        lb.append(l)
        ub.append(u)
    return lb, ub


def binned_count(length, generator, prime, modulo, number_of_bins):
    count, _min, _max = tuple_count(length, generator, prime, modulo)
    _min = floor(0.9*_min)
    _max = ceil(1.1*_max)
    bin_len = int( (_max-_min)/number_of_bins)
    pbin = _min
    cbin = bin_len
    ret = {}
    while cbin < _max:
        ret[cbin] = 0
        for c in count.values():
            if (pbin < c) and (c <= cbin):
                ret[cbin] += 1
        pbin = cbin
        cbin += bin_len
    return ret
