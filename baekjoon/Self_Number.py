#https://www.acmicpc.net/problem/4673

arr = []
l = []

for x in range(1, 10000):
    if x // 10 < 1:
        # 한자리
        arr.append(x + x)
    if x // 10 < 10:
        # 두자리
        arr.append(x + x // 10 + x % 10)
    if x // 100 < 10:
        # 세자리
        arr.append(x + x // 100 + x // 10 + x % 10)
    if x // 1000 < 10:
        # 네자리
        arr.append(x + x // 1000 + x // 100 + x // 10 + x % 10)
    if x == 10000:
        arr.append(x + x // 10000 + x // 1000 + x // 100 + x // 10 + x % 10)
    if not x in arr:
        l.append(x)


print(l)
