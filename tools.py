def is_palindromic(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
