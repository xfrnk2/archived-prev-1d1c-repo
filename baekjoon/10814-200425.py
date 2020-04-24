# 주소 : https://www.acmicpc.net/problem/10814
from operator import itemgetter

arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split()))+[i] for i in range(int(input()))]

arr.sort(key=itemgetter(0, 2))
for x in arr:
    print(f"{x[0]} {x[1]}")

