"""
Comparison of Various Prime number Generators, Prime Number Check algorithms

$python check_prime_number.py
Elapsed Time for check_prime: 28270.0014114 microseconds

Prime?: False
Elapsed Time for check_prime_opt: 0.0 microseconds

Prime?: False
Elapsed Time for check_prime_simple: 0.0 microseconds

Prime?: False
Elapsed Time for check_prime: 20199.9998093 microseconds

Prime?: True
Elapsed Time for check_prime_opt: 9.99927520752 microseconds

Prime?: True
Elapsed Time for check_prime_simple: 10.0016593933 microseconds

Prime?: True
Elapsed Time for get_primes_best: 9.99927520752 microseconds
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
Elapsed Time for get_primes_opt: 120.000839233 microseconds
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
Elapsed Time for get_primes_fastest: 30.0002098083 microseconds
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

"""

import time
import math
import functools

def timed(func):
    """
    Wrapper for Functions to print Time Consumed by each function
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        ITER = 100
        start = time.time()
        for x in xrange(ITER):
            result = func(*args, **kwargs)

        print "Elapsed Time for %s: %s microseconds"\
            % (func.__name__, (time.time() - start) * 1000000 / ITER)
        return result
    return wrapped


def get_primes(a, debug=False):
    """
    Non optimized function to list of prime numbers below a number
    """
    if not isinstance(a, int) or a < 0:
        raise Exception('Invalid Range')
    primes = set()
    #set implementation is little slower than list
    if a >= 2:
        primes.add(2)
    for x in xrange(2, a):
        for y in primes:
            if x % y == 0:
                break
        else:
            primes.add(x)
            continue
    return primes


def check_prime(a):
    """
    Noob way algorithm Highly looped and time consuming,
    Gets list of primes below the number, divides the number with each prime
    """
    divisibility = [x for x in get_primes(a) if a % x == 0]
    if a == 2 or not len(divisibility):
        return True
    return False


def get_primes_opt(a, debug=False):
    """Generate list of prime numbers under a number"""
    if not isinstance(a, int) or a < 0:
        raise Exception('Invalid Range')
    primes = list()
    if a >= 2:
        primes.append(2)
    for x in xrange(3, a, 2):
        for y in primes:
            if x % y is 0:
                break
        else:
            primes.append(x)
            continue
    return primes


def check_prime_opt(a):
    """
    Optimized search, find only prime numbers below the
    number's square root +1,
    Divides the given number with each of the item in prime list above.
    """
    if a == 2 or not len(
        [x for x in xrange(3, int(a ** .5 + 1), 2) if a % x is 0]
    ):
    #Return 'Prime' if input no is 2 or
        return True
    return False


def check_prime_simple(a):
    """
    Easiest and quickest way to find prime numbers
    Divide the given number with each odd number
    between 3 and square root + 1 of the given number.
    If there any full division, the number is not prime
    """
    if a is 2:
        return True
    for x in xrange(3, int(math.sqrt(a) + 1), 2):
        if a % x is 0:
            return False
            break
    return True


def get_primes_fastest(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def get_primes_best(a):
    """ Generate an infinite sequence of prime numbers.
    Optimzed algorithm

    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    # The running integer that's checked for primeness
    q = 2
    while q <= a:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

if __name__ == "__main__":
    def start():
        print "\nPrime?: %s" % timed(check_prime)(5000)
        print "\nPrime?: %s" % timed(check_prime_opt)(5000)
        print "\nPrime?: %s" % timed(check_prime_simple)(5000)
        print "\nPrime?: %s" % timed(check_prime)(4093)
        print "\nPrime?: %s" % timed(check_prime_opt)(4093)
        print "\nPrime?: %s" % timed(check_prime_simple)(4093)
        print "Primes: %s" % [x for x in timed(get_primes_best)(200)]
        print "Primes: %s" % timed(get_primes_opt)(200)
        print "Primes: %s" % timed(get_primes_fastest)(200)
    #cProfile.run('start()')
    start()
