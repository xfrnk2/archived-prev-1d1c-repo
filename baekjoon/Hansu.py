# https://www.acmicpc.net/problem/1065
n = int(input())
result = 0
for x in range(1, n+1):
    if x < 100:
        result += 1
        continue
    if x//100 - x//10%10 == x//10%10 - x%10:
        result += 1
print(result)