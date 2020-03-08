def func(n: int, arr: list):
    if n <= 0:
        return 0
    return func(n-1, arr) + arr[n-1]
print(func(5, [5, 4, 3, 2, 1]))