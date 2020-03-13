def func(p, q):
    if q == 0:
        return p
    return func(q, p%q)


def euclid(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return 1

def euclid2(m, n):
    if n == 0:
        return m
    return euclid2(n, m%n)

print(func(4, 100))
print(euclid(4, 100))
print(euclid2(4, 100))