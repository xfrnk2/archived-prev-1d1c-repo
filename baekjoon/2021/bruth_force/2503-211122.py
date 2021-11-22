# https://www.acmicpc.net/problem/2503

from itertools import permutations

N = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    t, s, b = input().split()
    t = list(map(int, t))
    s, b = int(s), int(b)
    remove_cnt = 0
    for i in range(len(num)):
        s_cnt = 0
        b_cnt = 0
        i -= remove_cnt
        for j in range(3):
            if t[j] in num[i]:
                if t[j] == num[i][j]:
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt == s and b_cnt == b:
            continue
        remove_cnt += 1
        num.remove(num[i])
    print(len(num))
