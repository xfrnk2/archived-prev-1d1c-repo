# 링크 : https://www.acmicpc.net/problem/2748
n = int(input())
result = {1:1, 2:1}
if 0 < n <= 90 :
    if n <= 2:
        print(result[n])
    else:
        for x in range(3, n+1):
            result[x] = result[x-1] + result[x-2]
        print(result[n])
