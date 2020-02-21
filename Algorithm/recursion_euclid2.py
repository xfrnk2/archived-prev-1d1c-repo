def func(p, q):
    if q == 0:
        return p
    return func(q, p%q)

print(func(4, 100))