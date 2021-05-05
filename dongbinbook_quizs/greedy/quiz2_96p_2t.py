m, n = map(int, input().split())
answer = 0
for _ in range(m):
    data = list(map(int, input().split()))
    min_value = min(data)
    answer = max(min_value, answer)
print(answer)