# https://www.acmicpc.net/problem/16953

a, b = map(int, input().split())
res = -1
que = [(a, 1)]
while que:
    crr_num, cnt = que.pop(0)
    if crr_num == b:
       res = cnt
       break

    if crr_num * 2 <= b:
        que.append((crr_num * 2, cnt + 1))
    if crr_num * 10 + 1 <= b:
        que.append((crr_num * 10 + 1, cnt + 1))

print(res)