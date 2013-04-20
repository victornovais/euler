# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from tools import is_prime

primes = []
n = 3
primes.append(2)
while len(primes) <= 10000:
    if is_prime(n):
        primes.append(n)
    n += 2

print primes[10000]