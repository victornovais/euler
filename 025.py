# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

n, m = 1, 2
term = 3
while True:
    n, m = m, n + m
    term += 1
    if len(str(m)) >= 1000:
        break

print term