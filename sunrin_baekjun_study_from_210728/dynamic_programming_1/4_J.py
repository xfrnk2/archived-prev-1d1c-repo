# https://www.acmicpc.net/problem/7579
# 메모리 초과가 난다. 다시 풀어보자.
N, M = map(int, input().split())
memory = sorted(list(map(int, input().split())))
cost = sorted(list(map(int, input().split())))
arr = [(0, 0)]
for i, j in zip(memory, cost):
    arr.append((i, j))
memory.insert(0, 0)

field = [[[0, 0]] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][0] <= j:

            k = max(field[i-1][j][0], arr[i][0] + field[i-1][j-arr[i][0]][0])
            v = max(field[i-1][j][1], arr[i][1] + field[i-1][j-arr[i][0]][1])
            field[i][j] = [k, v]
        else:
            field[i][j] = field[i-1][j]
bb = list(filter(lambda x: x[0]==M, [field[i][M] for i in range(N)]))
print(bb[0][1])
#print(sorted(bb, key=lambda x: x[1]))
