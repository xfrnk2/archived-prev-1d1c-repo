def euclid(m, n):
    if m < n:
        m, n = n, m

    if n == 0:
        return m
    return euclid(n, m%n)


print(euclid(60,12))