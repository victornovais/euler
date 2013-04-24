# The following iterative sequence is defined for the set of positive integers:
#
# n ->  n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

cache = {1: 1}
max_chain = (0, 0)


def chain(n):
    if not n in cache:
        cache[n] = chain(3*n+1 if n%2 else n/2) + 1
    return cache[n]


for i in range(3, 1000000, 2):
    chain_lenght = chain(i)
    if chain_lenght > max_chain[1]:
        max_chain = (i, chain_lenght)

print max_chain