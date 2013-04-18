def is_palindromic(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

