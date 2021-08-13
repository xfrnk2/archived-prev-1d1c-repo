# https://www.acmicpc.net/problem/1931

N = int(input())
c = []
for _ in range(N):
    c.append(tuple(map(int, input().split())))

c.sort(key=lambda x:(x[1], x[0]))
count = 1
now = c[0][1]
for i in range(1, len(c)):
    x, y = c[i]
    if now <= x:
        now = y
        count += 1

print(count) #



