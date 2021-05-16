import math
import numpy
from bisect import bisect_left

def primes_up_to(upto=1000000):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return numpy.insert(primes[isprime],0,2)

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def primes_starting_at(start=1000000, upto=2000000):
    assert(start < upto)
    p = primesfrom2to(upto)
    return p[bisect_left(p, start):]

if __name__ == "__main__":
    #print(primes_starting_at(1000000, 1100000))
    print(primesfrom2to(2000000))