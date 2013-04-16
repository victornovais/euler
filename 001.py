# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Using the formula of the sum of first n numbers
def sum(number, divisor):
    number = int(number / divisor)
    return int(number * (number + 1) / 2 * divisor)

limit = 999
print(sum(limit,3) + sum(limit,5) - sum(limit,15))
