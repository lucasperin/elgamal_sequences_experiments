from math import gcd
from functools import lru_cache


def element_at(position, generator, prime, modulo):
    return pow(generator, position, prime) % modulo

@lru_cache(maxsize=128)
def first_generator(prime):
    found = False
    g = 2
    while not found:
        found = True
        for i in range(1, prime-1):
            if element_at(i, g, prime, prime) == 1:
                found = False
                g +=1
                break
    return g

@lru_cache(maxsize=128)
def n_generators(n, prime):
    g = first_generator(prime)
    gens = [g]
    for i in range(2, prime-1):
        if gcd(i, prime-1) == 1:
            gens.append(element_at(i, g, prime, prime))
        if len(gens) >= n:
            break
    return gens

if __name__ == '__main__':
    print(sorted(n_generators(1020137, 1020137))[:20])

