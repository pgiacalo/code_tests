"""
This module compares the performance of cpu-intensive operations performed three different ways:
    - serially
    - using multiple threads, and
    - using a multiprocessing pool.

It demonstrates how threading is actually slower than serial and how a
multiprocessor pool achieves true parallelism for the fastest performance.
"""

import time
import threading as th
from multiprocessing import Pool
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    1099726899285419]


def is_prime(n):
    """Determines whether the given number is a prime. Returns True of False"""
    if n % 2 == 0:
        print(n, "is NOT prime")
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            print(n, "is NOT prime")
            return False
    print(n, "is prime")
    return True

def do_serial_test():
    """Performs a prime test on the list of PRIMES serially"""
    t1 = time.time()
    print ('Serial test starting...')
    # print prime(start), prime(start + 1), prime(start + 2), prime(start + 3)
    for number in PRIMES:
        is_prime(number)
    print ('----- Serial test took %.2f seconds' % (time.time() - t1))


def do_threading_test():
    """Performs a prime test on the list of PRIMES using thread """
    print ('Threading test starting...')
    jobs = []
    for number in PRIMES:
        jobs.append(th.Thread(target=is_prime, args=([number])))
    t1 = time.time()
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ('----- Multithreaded test took %.2f seconds' % (time.time() - t1))


def do_multiprocessing_pool_test():
    """Performs a prime test on the list of PRIMES using a multiprocessing pool"""
    print ('Multiprocessing Pool Test starting...')
    pool = Pool(len(PRIMES))              # start a worker process for each prime
    t1 = time.time()
    result = pool.map(is_prime, PRIMES)
    print ('----- Multiprocessing pool test took %.2f seconds' %(time.time() - t1))
    print('Results', result)

# is_prime(17)
do_serial_test()
print('----------------------------------------')
do_threading_test()
print('----------------------------------------')
do_multiprocessing_pool_test()
print('----------------------------------------')
