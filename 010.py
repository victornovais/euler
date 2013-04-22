# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from tools import is_prime

primes = [2]
for i in range(3, 2 * 10 ** 6, 2):
    if is_prime(i):
        primes.append(i)

print sum(primes)