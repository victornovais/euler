# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

first_primes = [2, 3, 5, 7, 11, 13, 17, 19]
other_numbers = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
number = 2520

while True:
    number += 10
    if all(number % i == 0 for i in first_primes):
        if all(number % i == 0 for i in other_numbers):
            break

print number