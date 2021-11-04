def solution(n, computers):
    visits = [0] * n
    ans = 0

    def func(idx):
        visits[idx] = 1
        for i, j in enumerate(computers[idx]):
            if idx != i and visits[i] == 0 and j == 1:
                func(i)

    for i in range(n):
        if visits[i] == 0:
            ans += 1
            func(i)
    return ans