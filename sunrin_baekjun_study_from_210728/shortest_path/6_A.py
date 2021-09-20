# https://www.acmicpc.net/problem/16953

a, b = map(int, input().split())
res = 0
que = [(a, 1)]
while que:
    crr_num, cnt = que.pop()
    if crr_num == b:
       result = cnt
       break

    if crr_num * 2 <= b:
        que.append((crr_num * 2, cnt + 1))
    if crr_num * 10 + 1 <= b:
        que.append((crr_num * 10 + 1, cnt + 1))

print(cnt)