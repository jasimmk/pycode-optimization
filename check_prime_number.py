"""
Comparison of Various Prime number Generators, Prime Number Check algorithms
"""

import time
import math


def timed(func):
    """
    Wrapper for Functions to print Time Consumed by each function
    """
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(args, kwargs)
        print "Elapsed Time for %s: %s" % (func.__name__, time.time() - start)
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
        ITER = 100
        y = ""
        start = time.time()
        for i in xrange(ITER):
                y = check_prime(5000)
        end = time.time()
        print (
            'Time per iteration for check_prime = %s microseconds ' %
            ((end - start) * 1000000 / ITER))
        print "Prime?: %s" % y

        z = ""
        startz = time.time()
        for i in xrange(ITER):
                z = check_prime_opt(5000)
        endz = time.time()
        print (
            'Time per iteration for check_prime_opt = %s microseconds ' %
            ((endz - startz) * 1000000 / ITER))
        print "Prime?: %s" % z

        m = ""
        startm = time.time()
        for i in xrange(ITER):
                m = check_prime_simple(5000)
        endm = time.time()
        print (
            'Time per iteration for check_prime_simple = %s microseconds ' %
            ((endm - startm) * 1000000 / ITER))
        print "Prime?: %s" % m

        startm = time.time()
        for i in xrange(ITER):
                n = [x for x in get_primes_best(200)]
        endm = time.time()
        print (
            'Time per iteration for get_primes_best = %s microseconds ' %
            ((endm - startm) * 1000000 / ITER))
        print "Primes: %s" % n

        startm = time.time()
        for i in xrange(ITER):
                n = get_primes_opt(200)
        endm = time.time()
        print (
            'Time per iteration for get_primes_opt = %s microseconds ' %
            ((endm - startm) * 1000000 / ITER))
        print "Primes: %s" % n

        startm = time.time()
        for i in xrange(ITER):
                n = get_primes_fastest(200)
        endm = time.time()
        print (
            'Time per iteration for get_primes_fastest = %s microseconds ' %
            ((endm - startm) * 1000000 / ITER))
        print "Primes: %s" % n
    #cProfile.run('start()')
    start()
