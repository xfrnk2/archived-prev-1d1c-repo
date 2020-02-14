#https://www.acmicpc.net/status?user_id=xfrnk2&problem_id=1546&from_mine=1

n = int(input())
values = list(map(int, input().split()))

result = 0
a = max(values)
for x in values:
    result += x/a * 100
print(result/n)
