# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


number = 600851475143
divisor = 2
while divisor * divisor <= number:
    if not number % divisor:
        number /= divisor
        large_factor = number
    else:
        if divisor > 2:
            divisor += 1
        divisor += 1

print large_factor