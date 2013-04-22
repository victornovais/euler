# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

try:
    for m in range(1, 500):
        for n in range(1, 500):
            if m < n:
                a, b, c = n ** 2 - m ** 2, 2 * m * n, n ** 2 + m ** 2
                if (a + b + c) == 1000:
                    raise StopIteration
except:
    print a, b, c
    print a * b * c


