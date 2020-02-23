def gcd(m: int, n: int) -> int:
    if m < n:
        m, n = n, m

    if m % n == 0:
        return n

    return gcd(n, m%n)

print(gcd(100, 12))
