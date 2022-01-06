# https://www.acmicpc.net/problem/10451

IS_VISITED_IDX = 2
VALUE_IDX = 1

T = int(input())
for _ in range(T):
    N = int(input())
    per = list(map(int, input().split()))
    per_arr = [[i + 1, per[i], False] for i in range(N)]
    count = 0
    for i in range(N):
        if per_arr[i][IS_VISITED_IDX]:
            continue
        pos = i
        while not per_arr[pos][IS_VISITED_IDX]:
            per_arr[pos][IS_VISITED_IDX] = True
            pos = per_arr[pos][VALUE_IDX] - 1
            if i == pos:
                break
        count += 1
    print(count)
