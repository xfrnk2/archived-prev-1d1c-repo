# https://www.acmicpc.net/problem/19532
a, b, c, d, e, f = list(map(int, input().split()))
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
