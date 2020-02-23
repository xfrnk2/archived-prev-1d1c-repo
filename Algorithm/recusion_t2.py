def intsum(n):
    if n == 0:
        return n
    return n + intsum(n-1)

def doublepower(x, n):
    if n == 0:
        return 1
    return x * doublepower(x, n-1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def euclid1(m, n):
    if m < n:
        m, n = n, m

    if m % n == 0:
        return n
    return euclid1(n, m%n)

def euclid2(p, q):
    if q == 0:
        return p
    return euclid2(q, p%q)




