def func(x: int, n: int) -> int:
    if n == 0:
        return 1
    return x * func(x, n-1)

print(func(2, 3))