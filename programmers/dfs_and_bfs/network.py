# lv3

def solution(n, computers):
    d = [0] * n
    ans = 0

    def func(idx):
        d[idx] = 1
        for j, k in enumerate(computers[idx]):
            if j != idx and k == 1 and d[j] != 1:
                func(j)

    for i in range(n):
        if d[i] == 0:
            ans += 1
            func(i)
    return ans

