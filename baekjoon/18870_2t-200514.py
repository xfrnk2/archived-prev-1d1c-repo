# 링크 : https://www.acmicpc.net/problem/18870

input()
arr = list(map(int, input().split()))
values_by_key = {}
for i,j in enumerate(sorted(set(arr))):
    values_by_key[j] = i
for x in arr:
    print(values_by_key[x], end=' ')