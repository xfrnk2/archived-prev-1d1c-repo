# https://www.acmicpc.net/problem/2417

# 첫번째 풀이. 하지만 이분탐색으로 풀지 않았기에 꽝이다. 다시 풀어야겠다.
# from math import ceil
# n = int(input())
# print(ceil(n ** 0.5) if float(n ** 0.5) else int(n**0.5))


# 두번째 풀이. 잘 동작한다.
n = int(input())

start, end = 0, n
while start < end:
    m = (start + end)//2

    if n > m**2:
        start = m+1
    else:
        end = m

print(start)