# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print (100 * (100 + 1) / 2) ** 2 - sum(i ** 2 for i in range(1, 101))

